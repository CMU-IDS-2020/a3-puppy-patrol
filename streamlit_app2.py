import streamlit as st
import pandas as pd
import altair as alt

st.title("""
        # Aww Rats!🐀
        An exploration of rat sightings in New York City, courtesy of [NYC Open Data](https://data.cityofnewyork.us/Social-Services/Rat-Sightings/3q43-55fe).
        """)


alt.data_transformers.disable_max_rows()


def load_vis(df, type="random"):
    if(type == "random"):
        df_elements = df.sample(n=min(5, df.shape[0]))
        selected_c = []
        for index, row in df_elements.iterrows():
            title = posts[posts["id"] == row["post_id"]]["title"].values[0]
            selected_c.append((title, row['comment_body'], row["sentiment"]))
        df2 = comments_all.copy()
        df2["in"] = df2.apply(lambda r: r["comment_id"] in df["comment_id"].values, axis=1)
        return (selected_c, load_bar_chart(df2))

def load_bar_chart(comments):
    if(comments.shape[0] == 0):
        print("No data")
        return
    chart = alt.Chart(comments).mark_bar(size=90).encode(
        x='sentiment',
        y='count(sentiment)',
        color='in'
    ).properties(
        height=240,
        width=400
    )
    st.write(chart)
    
def f(row, keyword):
    if(not isinstance(row["tokenized_text"], str)):
        return False
    return (row["tokenized_text"].find(keyword) >= 0)

def filter_by_keyword(dataset, keyword):
    if(keyword is None):
        return dataset
    return dataset[dataset.apply(lambda row: f(row, keyword.lower()), axis=1)]

comments_all = pd.read_csv("final_data/reddit_visualization/rat_comments.csv")
comments_positive = comments_all[comments_all["sentiment"] == "Positive"]
comments_negative = comments_all[comments_all["sentiment"] == "Negative"]
comments_neutral = comments_all[comments_all["sentiment"] == "Neutral"]

posts = pd.read_csv("final_data/reddit_visualization/rat_posts.csv")
keywords = pd.read_csv("final_data/reddit_visualization/keywords.csv")

currently_selected_sentiment = None
currently_selected_keyword = None
current_df = comments_all

def reload():
    dynamic_markdown = '''
        ### Comments
    '''
    
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
        color = "green"
        if(i[2] == "Negative"):
            color = "red"
        elif(i[2] == "Neutral"):
            color = "black"
        dynamic_markdown += ('<div style="font-style: italic; color:grey">' + ("Post title: " + str(i[0])) + '</div>')
        dynamic_markdown += ('<div style="padding: 12px 0px; border-bottom: 1px solid grey;' + "color:" + color + '">' + str(i[1]) + '</div>')
    return dynamic_markdown
    
md = reload()

st.markdown(md, unsafe_allow_html=True)

