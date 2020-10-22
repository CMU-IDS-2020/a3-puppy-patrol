import re
import numpy as np
import pandas as pd
import altair as alt
import pydeck as pdk
import streamlit as st
from datetime import datetime
import streamlit.components.v1 as components

st.markdown(
    """
        <h1 style="font-family: serif;">Aww Rats!🐀</h1>
        <h2 style="font-family: serif;"> Who Runs New York?</h2>
        """,
    unsafe_allow_html=True,
)
st.write(
    """
        Rats are as synonymous with New York City as trains, the Empire State Building, and expensive apartments. There is even a [Wikipedia page dedicated to Rats in New York City](https://en.wikipedia.org/wiki/Rats_in_New_York_City). While cute and furry creatures, rats are also disease vectors (not that we need more of those right now). The City even went so far as to make a [$32 million plan](https://www.nytimes.com/2017/07/12/nyregion/new-york-city-rat-problem.html) to control the rodent problem.
        According to [NYC Open Data](https://data.cityofnewyork.us/Social-Services/Rat-Sightings/3q43-55fe) the number of reports of rat sightings has been on an upward trend.
        """
)
components.iframe("https://connie.dog/rat-image-tsne/", width=700, height=1000)

st.write(
    "<style>div.Widget.row-widget.stRadio > div{flex-direction:row;}</style>",
    unsafe_allow_html=True,
)


domain = ["Positive", "Negative", "Neutral"]
range_ = ["#33BB44", "#BB2233", "#9999AA"]

input_dropdown = alt.binding_select(options=["Europe", "Japan", "USA"])
selection = alt.selection_single(
    fields=["Origin"], bind=input_dropdown, name="Country of "
)
color = alt.condition(
    selection, alt.Color("Origin:N", legend=None), alt.value("lightgray")
)


def load_vis(df, type="random"):
    if type == "random":
        df_elements = df.sample(n=min(3, df.shape[0]))
        selected_c = []
        for index, row in df_elements.iterrows():
            title = posts[posts["id"] == row["post_id"]]["title"].values[0]
            selected_c.append(
                (title, row["comment_body"], row["sentiment"], row["comment_score"])
            )
        # df2 = comments_all.copy()
        # df2["in"] = df2.apply(lambda r: r["comment_id"] in df["comment_id"].values, axis=1)
        return (selected_c, load_bar_chart(df))


def load_bar_chart(comments):
    if comments.shape[0] == 0:
        print("No data")
        return
    chart_all = (
        alt.Chart(comments_all)
        .mark_bar(size=70, opacity=0.2)
        .encode(
            y=alt.X("sentiment", axis=alt.Axis(domain=False, title=None)),
            x=alt.X("count(sentiment)", axis=None),
            color=alt.Color(
                "sentiment", scale=alt.Scale(domain=domain, range=range_), legend=None
            ),
        )
    )

    chart = (
        alt.Chart(comments)
        .mark_bar(size=70, opacity=0.6)
        .encode(
            y="sentiment",
            x=alt.X("count(sentiment)", axis=None),
            color=alt.Color(
                "sentiment", scale=alt.Scale(domain=domain, range=range_), legend=None
            ),
        )
    )

    text = chart.mark_text(align="left", baseline="middle", dx=3, dy=0).encode(
        detail="site:N", text="count(sentiment):Q"
    )

    st.write(
        (chart_all + chart + text)
        .configure_axis(grid=False)
        .configure_view(strokeWidth=0)
        .properties(height=300, width=700)
    )


def f(row, keyword):
    if not isinstance(row["tokenized_text"], str):
        return False
    return (
        row["tokenized_text"].find(keyword + " ") >= 0
        or row["tokenized_text"].find(" " + keyword) >= 0
    )


def filter_by_keyword(dataset, keyword):
    if keyword is None or keyword == "":
        return dataset
    return dataset[dataset.apply(lambda row: f(row, keyword.lower()), axis=1)]


comments_all = pd.read_csv("final_data/reddit_visualization/rat_comments.csv")
comments_positive = comments_all[comments_all["sentiment"] == "Positive"]
comments_negative = comments_all[comments_all["sentiment"] == "Negative"]
comments_neutral = comments_all[comments_all["sentiment"] == "Neutral"]

posts = pd.read_csv("final_data/reddit_visualization/rat_posts.csv")
keywords = pd.read_csv("final_data/reddit_visualization/keywords.csv")

genre = st.radio("Filter by sentiment", ("All", "Negative", "Neutral", "Positive"))

f_keywords = keywords[keywords["Sentiment"] == genre]
print(f_keywords["Keyword"].values)

cspk = st.radio(
    "Filter by key phrases",
    np.concatenate(
        (
            np.array(["Show all comments", "Custom keyword"]),
            f_keywords["Keyword"].values,
        )
    ),
)

currently_selected_keyword = cspk
if cspk == "Show all comments":
    currently_selected_keyword = None
elif cspk == "Custom keyword":
    currently_selected_keyword = st.text_input(
        "Search keywords:", value="", max_chars=None, key=None, type="default"
    )

currently_selected_sentiment = genre

currently_selected_preset_keywords = None
current_df = comments_all


def reload():
    if currently_selected_keyword == None:
        dynamic_markdown = (
            "<p> 3 randomly selected out of " + genre + " Comments" + "</p>"
        )
    else:
        dynamic_markdown = (
            "<p> 3 randomly selected out of "
            + genre
            + " Comments with the keywords: "
            + currently_selected_keyword
            + "</p>"
        )

    dynamic_markdown += "\n"

    if currently_selected_sentiment == "Positive":
        current_df = comments_positive
    elif currently_selected_sentiment == "Negative":
        current_df = comments_negative
    elif currently_selected_sentiment == "Neutral":
        current_df = comments_neutral
    else:
        current_df = comments_all
    final_df = filter_by_keyword(current_df, currently_selected_keyword)
    (selected_c, vis) = load_vis(final_df)
    for i in selected_c:
        color = range_[0] + "11"
        if i[2] == "Negative":
            color = range_[1] + "11"
        elif i[2] == "Neutral":
            color = range_[2] + "11"
        body = str(i[1]).replace("\r", " ").replace("\n", " ")
        body_s = re.sub(
            r"(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)", "", body
        )
        print(repr(body))
        dynamic_markdown += (
            '<div style="max-height: 200px; overflow: scroll; border: 1px solid grey; padding: 12px; border-radius: 12px; margin-bottom: 12px; font-size: 12px;'
            + "background-color:"
            + color
            + '">\n'
        )
        dynamic_markdown += (
            '<div style="font-style: italic; color:grey">'
            + ("Post title: " + str(i[0]) + " (" + str(i[3]) + " upvotes)")
            + "</div>"
        )
        dynamic_markdown += (
            '<div style="line-height: 120%; padding: 12px 0px;">' + body_s + "</div>"
        )
        dynamic_markdown += "\n</div>"
    return dynamic_markdown


md = reload()

st.markdown(md, unsafe_allow_html=True)

# Using URLs for df > 5k rows
rats_url = "https://raw.githubusercontent.com/CMU-IDS-2020/a3-puppy-patrol/master/rat_activity.csv"
budget_url = "https://raw.githubusercontent.com/CMU-IDS-2020/a3-puppy-patrol/master/nycdoh_budget.csv"
sightings_url = (
    "https://raw.githubusercontent.com/CMU-IDS-2020/a3-puppy-patrol/master/rats.csv"
)

nyc_geojson_url = "https://raw.githubusercontent.com/CMU-IDS-2020/a3-puppy-patrol/master/2010_Census_Blocks.geojson"
nyc_geojson = alt.Data(
    url=nyc_geojson_url, format=alt.DataFormat(property="features", type="json")
)

df = pd.read_csv(rats_url)

boroughs = list(df["borough"].unique())
boroughs.append("All")
boroughs.reverse()
borough = st.radio("Select Borough", boroughs)
df_borough = df if borough == "All" else df[df["borough"] == borough]

brush = alt.selection(type="interval", encodings=["x"])

chart = (
    alt.Chart(df_borough)
    .mark_line()
    .encode(
        x=alt.X("inspection_date:T", timeUnit="year", title="Inspection Date"),
        y=alt.Y("count(unique_key):Q", title="Count of Inspections"),
    )
    .properties(width=640, height=200)
).add_selection(brush)

chart2 = (
    alt.Chart(df_borough)
    .mark_circle(opacity=0.005)
    .encode(longitude="longitude", latitude="latitude")
    .properties(width=640, height=500)
    .transform_filter(brush)
)

map_bg = (
    alt.Chart(nyc_geojson)
    .mark_geoshape(fill="none", stroke="#ccc", strokeWidth=0.1)
    .encode()
)

st.write(chart & (map_bg + chart2))


df_budget_raw = pd.read_csv(budget_url)
df_budget = df_budget_raw.groupby("Fiscal Year").mean().reset_index()
df_budget["year"] = df_budget["Fiscal Year"].apply(lambda d: f"{d}-01-01")
chw = 275

chart = (
    alt.Chart(df_budget, title="Total Budget Trends")
    .mark_line()
    .encode(
        x="year:T", y=alt.Y("Current Modified Budget Amount:Q", title="Fiscal Year")
    )
    .properties(width=chw)
)

dfb_bool = df_budget_raw["Budget Code Name"].apply(lambda d: "Pest" in d)
dfb = df_budget_raw[dfb_bool].groupby("Fiscal Year").mean().reset_index()
dfb["year"] = dfb["Fiscal Year"].apply(lambda d: f"{d}-01-01")

chart2 = (
    alt.Chart(dfb, title="Pest Control Budget Trends")
    .mark_line()
    .encode(
        x="year:T", y=alt.Y("Current Modified Budget Amount:Q", title="Fiscal Year")
    )
    .properties(width=chw)
)

st.write(chart | chart2)

chart2 = (
    alt.Chart(dfb)
    .mark_line()
    .encode(
        x="year:T", y=alt.Y("Current Modified Budget Amount:Q", title="Fiscal Year")
    )
    .properties(width=700)
)

dfs_bool = df_budget_raw["Budget Code Name"].apply(lambda d: "Sanitation" in d)
dfs = df_budget_raw[dfs_bool].groupby("Fiscal Year").mean().reset_index()
dfs["year"] = dfs["Fiscal Year"].apply(lambda d: f"{d}-01-01")

chart = (
    alt.Chart(dfs, title="Sanitation vs Pest Control Budget")
    .mark_line(stroke="crimson")
    .encode(
        x="year:T", y=alt.Y("Current Modified Budget Amount:Q", title="Fiscal Year")
    )
)

st.write(chart + chart2)
