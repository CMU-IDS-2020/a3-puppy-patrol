import re
import numpy as np
import pandas as pd
import altair as alt
import pydeck as pdk
import streamlit as st
from datetime import datetime
import streamlit.components.v1 as components

font_fam = "serif"


def h2(s: str):
    st.markdown(
        f"""
    <h2 style="font-family: {font_fam};">{s.title()}</h2>
    """,
        unsafe_allow_html=True,
    )


st.markdown(
    f"""
        <h1 style="font-family: {font_fam};">Aww Rats!🐀</h1>
        """,
    unsafe_allow_html=True,
)
st.write(
    f"""
    For several years in a row, New York has been given the dubious honor of being in the top three “Rattiest” cities in the United States, as ranked by Orkin, a national pest control service. New York has also been crowned the "Worst Rat City in the World" by Animal Planet in 2014, and "USA's No. 1 Pestropolis” by rodentologist Bobby Corrigan.

New Yorkers have always been forced to coexist with rats. However, the rat problem has grown steadily over time all across the city, especially in Brooklyn and Manhattan, thus increasing their visibility and worrying residents.

> “So many rats regularly lurk on a sidewalk in Brooklyn that it is the humans who avoid the rats, not the other way around.” - Winne Chan, New York Times.
"""
)

h2("Basic Information About Rats")

st.write(
    """
The city’s rat population is dominated by the brown rat, also known as the Norway rat, the sewer rat, and the alley rat. The species is believed to have originated in East Asia, eventually migrating to Europe. The rats we see around the city today are descendants of those that came from Western Europe in the 1700s. Once the Norway rats arrived in NYC, they quickly killed off the smaller roof rats that inhabited the city, and they’ve continued thriving to this day. 

Rats are nocturnal and usually stay within 450 feet of their burrows, which are often in apartment floorboards, alleyways, vegetation, sidewalks or basements. Rats tend to look for places that provide them with food, water, shelter and safe ways for them to get around. 

They live in colonies of around 40–50 members and can be seen travelling in herds, passing
down successful feeding paths to younger generations. Solitary rats, especially those found during the day, have often been displaced from their burrows.

Rats are athletes and survivors! The adult rat can squeeze through holes or gaps 1 inch wide, jump a horizontal distance of up to 4 feet, survive a fall from a height of almost 40 feet, and tread water for three days.

Like humans, NYC rats are highly intelligent, have daily routines, communicate with one another, and have their own social order. 

> “A rat is so smart they notice when something new enters their environment and are highly suspicious. For example, older rats won’t eat a new food source. They’ll leave it out for the younger ones to see if they die from eating it. Only then will they venture out to try it.” - Bill Swan, rat specialist and co-owner of NYC Pest Control in Brooklyn.

Try out the visualization below to get a visual primer to where rats are found, where they make their habitats, and their cultural status in NYC history. Scroll to zoom, drag to pan, and click to enter and exit group viewing mode. The images from the visualization were scraped from Google Images and Flickr’s Creative Commons images. Images are displayed by visual similarity and were hand-labeled with general categories.

        """
)
components.iframe("https://connie.dog/rat-image-tsne/", width=700, height=1000)

st.write(
    "<style>div.Widget.row-widget.stRadio > div{flex-direction:row;}</style>",
    unsafe_allow_html=True,
)

h2("Rat Diseases")

st.write(
    """
Rats can spread disease and contaminate food sources. Leptospirosis, a bacterial infection spread by rat urine, killed one and sickened others in the Bronx in 2017. 

A survey conducted in 2014 studied 133 brown rats from residential buildings in Manhattan. While at least 18 of the viruses found are known to cause disease in humans, it is unclear how infectious the rats are to residents.

Peter Daszak, president of EcoHealth Alliance, called the study "shocking and surprising" and "a recipe for a public health nightmare"
"""
)

st.write(
    """
<table>
<tr><th>Fleas</th><td><table>
    <tr><td>Bubonic plague</td></tr>
    <tr><td>Typhus</td></tr>
    <tr><td>Spotted Fever</td></tr>
</table></td></tr>
<tr><th>Bacteria</th><td><table>
    <tr><td>E. coli</td></tr>
    <tr><td>Clostridium difficile</td></tr>
    <tr><td>Salmonella</td></tr>
</table></td></tr>
<tr><th>Viral</th><td><table>
    <tr><td>Rat-bite fever</td></tr>
    <tr><td>Tetanus from a bite</td></tr>
    <tr><td>Hemorrhagic fever by Seoul hantavirus</td></tr>
    <tr><td>sapoviruses</td></tr>
    <tr><td>cardioviruses</td></tr>
    <tr><td>kobuviruses</td></tr>
    <tr><td>parechoviruses</td></tr>
    <tr><td>rotaviruses</td></tr>
    <tr><td>hepaciviruses</td></tr>
</table></td></tr>
</table>
""",
    unsafe_allow_html=True,
)

h2("Additional Rat Problems")
st.write(
    """
* Gnawing and burrowing can cause structural damage.
* They have attacked homeless people, eaten cadavers in the city morgue, and bitten infants and young children to get food off their faces. 
*Rats have chewed clean through car engine wires.
"""
)

h2("Respect for Rats?")

st.write(
    """
Despite the overwhelming dislike for rats, some of those who study them, fight them, or encounter them often have developed a begrudging respect for the little creatures.

Graduate student Matthew Combs has come to respect the enemy after studying them for so long: “They are, quote-unquote, vermin, and definitely pests we need to get rid of,” he says, “but they are extraordinary in their own ways.” 

Ex-Manhattan Borough President Scott Stringer joked in 2013, "The rats don't scurry. They walk right up to you and say, 'How are you, Mr. Borough President?'”  

An anonymous woman who offers an online rat-killing gift service told the Guardian: “I don’t have it out for rats. I think they’re pretty impressive. There’s just too many of them.”

Mike Deutsch, a veteran rat-catcher at the New York-based Arrow Exterminating Company, said he has developed “a relationship with rats.”
> “They are an incredible animal, I admire their ability to adapt to different situations,” he said. “I look at them as a tremendous success.”

"""
)

h2("Internet Fame")
st.write(
    """
NYC rats have found  success online, making the “NYC rat” a meme and lesser cultural icon.
In 2011, a video of a rat climbing on a sleeping man's face on the subway went viral.
In 2015, a YouTube video of a rat carrying a slice of pizza in the subway went viral and garnered 5 million views within two days, and spawned similar staged videos with trained rats such as Selfie Rat.
In early 2016, another video of a rat climbing on a sleeping subway rider was uploaded to social media. That year, YouTube videos of rats on subway tracks and in a subway car in New York City went viral, as did videos of rats in a Dunkin' Donuts in Manhattan.

Individual reactions to NYC rats can be explored using the visualization below, which displays the results of sentiment analysis and keyword extraction of all Reddit comments on posts related to rats in New York.

"""
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


h2("How Widespread and Why?")

# Using URLs for df > 5k rows
rats_url = (
    "https://raw.githubusercontent.com/CMU-IDS-2020/a3-puppy-patrol/master/rats.csv"
)
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
boroughs = [d.title() for d in boroughs if d.lower() != "unspecified"]
boroughs.append("All")
boroughs.reverse()
borough = st.radio("Select Borough", boroughs)
df_borough = (
    df if borough == "All" else df[df["borough"].apply(lambda d: d.title()) == borough]
)

brush = alt.selection(type="interval", encodings=["x"])

chart = (
    alt.Chart(df_borough)
    .mark_line()
    .encode(
        x=alt.X("created_date:T", timeUnit="year", title="Sighting Report Date"),
        y=alt.Y("count(created_date):Q", title="Count of Sightings"),
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

st.write(
    """
There’s an urban myth that there are more rats than people in the five boroughs of New York City (8.4 million in 2020). Public health officials have not developed any reliable way to estimate their actual population numbers. However, a 2014 study by Jonathan Auerbach, which was reported in the Royal Statistical Society's Significance magazine, estimated that there were closer to 2 million rats in the city. 

Rats have an extremely high rate of reproduction, mating up to 20 times in 6 hours. A female rat
produces 4–7 litters of around 10 rats each year. Studies indicate New York is particularly well-suited for rats due to sanitation practices, climate, housing construction standards and more. Warmer weather due to climate change makes for longer mating seasons and an increase in rat populations. 

Rats primarily find food at human habitations, such as in the trash. A contributing factor to the rat population is how the city collects trash: bags are left outside overnight before pick up the next morning.

> “It’s just an all-night buffet for the rats,” Jason Munshi-South, a biology professor at Fordham University said. 

"""
)

# df_trash = df_trash.groupby("BOROUGH").count().reset_index()
# chart = (
#    alt.Chart(nyc_geojson)
#    .mark_geoshape(color="count(BOROUGH):Q")
#    .transform_lookup(
#        lookup="BOROUGH", from_=alt.LookupData(trash_url, key="BOROUGH")
#    )
# )
# st.write(chart)

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
