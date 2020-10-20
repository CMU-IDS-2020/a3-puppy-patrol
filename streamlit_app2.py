import streamlit as st
import pandas as pd
import altair as alt
import re
import numpy as np

st.write('<style>div.Widget.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)


domain = ["Positive", "Negative", "Neutral"]
range_ = ['#33BB44','#BB2233', "#9999AA"]

input_dropdown = alt.binding_select(options=['Europe','Japan','USA'])
selection = alt.selection_single(fields=['Origin'], bind=input_dropdown, name='Country of ')
color = alt.condition(selection,
                    alt.Color('Origin:N', legend=None),
                    alt.value('lightgray'))

def load_vis(df, type="random"):
    if(type == "random"):
        df_elements = df.sample(n=min(3, df.shape[0]))
        selected_c = []
        for index, row in df_elements.iterrows():
            title = posts[posts["id"] == row["post_id"]]["title"].values[0]
            selected_c.append((title, row['comment_body'], row["sentiment"], row["comment_score"]))
        #df2 = comments_all.copy()
        #df2["in"] = df2.apply(lambda r: r["comment_id"] in df["comment_id"].values, axis=1)
        return (selected_c, load_bar_chart(df))

def load_bar_chart(comments):
    if(comments.shape[0] == 0):
        print("No data")
        return
    chart_all = alt.Chart(comments_all).mark_bar(
        size=70, 
        opacity=0.2
    ).encode(
        y=alt.X('sentiment',axis=alt.Axis(domain=False, title=None)),
        x=alt.X('count(sentiment)', axis=None),
        color=alt.Color('sentiment', scale=alt.Scale(domain=domain, range=range_), legend=None)
    )
    
    chart = alt.Chart(comments).mark_bar(size=70,opacity=0.6).encode(
        y='sentiment',
        x=alt.X('count(sentiment)', axis=None),
        color=alt.Color('sentiment', scale=alt.Scale(domain=domain, range=range_), legend=None)
    )
    
    text = chart.mark_text(
        align='left',
        baseline='middle',
        dx=3,
        dy=0
    ).encode(
        detail='site:N',
        text='count(sentiment):Q'
    )
    
    st.write((chart_all + chart + text).configure_axis(
        grid=False
    ).configure_view(
        strokeWidth=0
    ).properties(
        height=300,
        width=700
    ))
    
def f(row, keyword):
    if(not isinstance(row["tokenized_text"], str)):
        return False
    return (row["tokenized_text"].find(keyword + " ") >= 0
           or row["tokenized_text"].find(" " + keyword) >= 0)

def filter_by_keyword(dataset, keyword):
    if(keyword is None or keyword == ""):
        return dataset
    return dataset[dataset.apply(lambda row: f(row, keyword.lower()), axis=1)]

comments_all = pd.read_csv("final_data/reddit_visualization/rat_comments.csv")
comments_positive = comments_all[comments_all["sentiment"] == "Positive"]
comments_negative = comments_all[comments_all["sentiment"] == "Negative"]
comments_neutral = comments_all[comments_all["sentiment"] == "Neutral"]

posts = pd.read_csv("final_data/reddit_visualization/rat_posts.csv")
keywords = pd.read_csv("final_data/reddit_visualization/keywords.csv")

genre = st.radio(
     "Filter by sentiment",
     ("All", 'Negative', 'Neutral', 'Positive'))

f_keywords = keywords[keywords["Sentiment"] == genre]
print(f_keywords["Keyword"].values)

cspk = st.radio(
     "Filter by key phrases", np.concatenate((np.array(["Show all comments", "Custom keyword"]), f_keywords["Keyword"].values)))

currently_selected_keyword = cspk
if(cspk == "Show all comments"):
    currently_selected_keyword = None
elif(cspk == "Custom keyword"):
    currently_selected_keyword = st.text_input("Search keywords:", value="", max_chars=None, key=None, type='default')

currently_selected_sentiment = genre

currently_selected_preset_keywords = None
current_df = comments_all

def reload():
    if(currently_selected_keyword == None):
        dynamic_markdown = '<p> 3 randomly selected out of ' + genre + ' Comments' + '</p>' 
    else:
        dynamic_markdown = '<p> 3 randomly selected out of ' + genre + ' Comments with the keywords: ' + currently_selected_keyword + '</p>' 
    
    dynamic_markdown += '\n'
    
    if (currently_selected_sentiment == "Positive"):
        current_df = comments_positive
    elif (currently_selected_sentiment == "Negative"):
        current_df = comments_negative
    elif (currently_selected_sentiment == "Neutral"):
        current_df = comments_neutral
    else:
        current_df = comments_all
    final_df = filter_by_keyword(current_df, currently_selected_keyword)
    (selected_c, vis) = load_vis(final_df)
    for i in selected_c:
        color = range_[0] + "11"
        if(i[2] == "Negative"):
            color = range_[1] + "11"
        elif(i[2] == "Neutral"):
            color = range_[2] + "11"
        body = str(i[1]).replace('\r', ' ').replace('\n', ' ')
        body_s = re.sub(r'(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)', '', body)
        print(repr(body))
        dynamic_markdown += ('<div style="max-height: 200px; overflow: scroll; border: 1px solid grey; padding: 12px; border-radius: 12px; margin-bottom: 12px; font-size: 12px;'+ "background-color:" + color + '">\n')
        dynamic_markdown += ('<div style="font-style: italic; color:grey">' + ("Post title: " + str(i[0]) + " (" + str(i[3]) + " upvotes)") + '</div>')
        dynamic_markdown += ('<div style="line-height: 120%; padding: 12px 0px;">' + body_s + '</div>')
        dynamic_markdown += ('\n</div>')
    return dynamic_markdown
    
md = reload()

st.markdown(md, unsafe_allow_html=True)

