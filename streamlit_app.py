import re
import numpy as np
import pandas as pd
import altair as alt
import pydeck as pdk
import streamlit as st
from datetime import datetime
import streamlit.components.v1 as components

font_fam = "Merriweather"
font_accent_color = "#175BC2"

st.write(
    "<style>@import url('https://fonts.googleapis.com/css2?family=Merriweather:ital,wght@0,300;0,700;1,300;1,700&display=swap'); div.Widget.row-widget.stRadio > div{flex-direction:row;} blockquote{font-size: 18px !important; font-weight: 700; font-family: Merriweather; color:"
    + font_accent_color
    + ";} </style>",
    unsafe_allow_html=True,
)


def h2(s: str):
    st.markdown(
        f"""
    <h2 style="font-family: {font_fam}; font-weight: 600; font-size: 30px;">{s.title()}</h2>
    """,
        unsafe_allow_html=True,
    )


def h3(s: str):
    st.markdown(
        f"""
    <h3 style="font-family: {font_fam}; margin-top: 12px; font-weight: 600; font-style: italic; font-size: 24px;">{s.title()}</h2>
    """,
        unsafe_allow_html=True,
    )


def instructions(s: str):
    st.markdown(
        f"""
    <p style="font-weight: 600; font-style: italic; color: rgba(0, 0, 0, 0.65)">{s}</p>
    """,
        unsafe_allow_html=True,
    )


st.markdown(
    f"""
        <h1 style="font-family: {font_fam}; font-weight: 900; font-size: 48px;">Aww Rats! What's up with the rat problem in NYC? 🐀 </h1>
        """,
    unsafe_allow_html=True,
)
st.write(
    f"""
    For several years in a row, New York has been given the dubious honor of being in the top three “Rattiest” cities in the United States, as ranked by Orkin, a national pest control service. New York has also been crowned the "Worst Rat City in the World" by Animal Planet in 2014, and "USA's No. 1 Pestropolis” by rodentologist Bobby Corrigan.

New Yorkers have always been forced to coexist with rats. However, the rat problem has grown steadily over time all across the city, especially in Brooklyn and Manhattan, thus increasing their visibility and worrying residents.

> “So many rats regularly lurk on a sidewalk in Brooklyn that it is the humans who avoid the rats, not the other way around.” - Winne Hu, New York Times.

Through this article, we will investigate all aspects of the rat problem in NYC, looking at both qualatative data and quantative data. We will introduce the rat problem, investigate how people are reacting to it, how widespread it is, and finally end on what policies the city government has taken to fight it.
"""
)

h2("About NYC rats")

st.write(
    """
Rats are nocturnal and usually stay within 450 feet of their burrows, which are often in apartment floorboards, alleyways, vegetation, sidewalks or basements. Rats tend to look for places that provide them with food, water, shelter and safe ways for them to get around. 

They live in colonies of around 40–50 members and can be seen travelling in herds, passing
down successful feeding paths to younger generations. Solitary rats, especially those found during the day, have often been displaced from their burrows.

Like humans, NYC rats are highly intelligent, have daily routines, communicate with one another, and have their own social order. 

> “A rat is so smart they notice when something new enters their environment and are highly suspicious. For example, older rats won’t eat a new food source. They’ll leave it out for the younger ones to see if they die from eating it. Only then will they venture out to try it.” - Bill Swan, rat specialist and co-owner of NYC Pest Control in Brooklyn.

        """
)

instructions(
    "Try out the visualization below to get a visual primer to where rats are found, where they make their habitats, and their cultural status in NYC history. Pinch (preferred) or scroll to zoom, drag to pan, and click to enter and exit group viewing mode. The images from the visualization were scraped from Google Images and Flickr’s Creative Commons images. Images are displayed by visual similarity and were hand-labeled with general categories"
)

components.iframe("https://connie.dog/rat-image-tsne/", width=700, height=800)


h3("Rat problems")

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

st.write(
    """
\nRats aren't just a source of disease. They've also been known to wreck havoc in other ways, such as:
* Gnawing and burrowing can cause structural damage.
* They have attacked homeless people, eaten cadavers in the city morgue, and bitten infants and young children to get food off their faces. 
*Rats have chewed clean through car engine wires.
"""
)

h3("Respect for Rats?")

st.write(
    """
Despite the overwhelming dislike for rats, some of those who study them, fight them, or encounter them often have developed a begrudging respect for the little creatures.

Graduate student Matthew Combs has come to respect the enemy after studying them for so long: 
> “They are, quote-unquote, vermin, and definitely pests we need to get rid of,” he says, “but they are extraordinary in their own ways.” 

Ex-Manhattan Borough President Scott Stringer joked in 2013, 
> "The rats don't scurry. They walk right up to you and say, 'How are you, Mr. Borough President?'”  

An anonymous woman who offers an online rat-killing gift service told the Guardian: 
> “I don’t have it out for rats. I think they’re pretty impressive. There’s just too many of them.”

Mike Deutsch, a veteran rat-catcher at the New York-based Arrow Exterminating Company, said he has developed “a relationship with rats.”
> “They are an incredible animal, I admire their ability to adapt to different situations,” he said. “I look at them as a tremendous success.”

"""
)

h3("Internet Fame")
st.write(
    """
NYC rats have found  success online, making the “NYC rat” a meme and lesser cultural icon.
In 2011, a video of a rat climbing on a sleeping man's face on the subway went viral.
In 2015, a YouTube video of a rat carrying a slice of pizza in the subway went viral and garnered 5 million views within two days, and spawned similar staged videos with trained rats such as Selfie Rat.
In early 2016, another video of a rat climbing on a sleeping subway rider was uploaded to social media. That year, YouTube videos of rats on subway tracks and in a subway car in New York City went viral, as did videos of rats in a Dunkin' Donuts in Manhattan.

"""
)

instructions(
    "Individual reactions to NYC rats can be explored using the visualization below, which displays the results of sentiment analysis and keyword extraction of all Reddit comments on posts related to rats in New York."
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


h2("How widespread is the rat problem and Why?")

st.write(
    """
There’s an urban myth that there are more rats than people in the five boroughs of New York City (8.4 million in 2020). Public health officials have not developed any reliable way to estimate their actual population numbers. However, a 2014 study by Jonathan Auerbach, which was reported in the Royal Statistical Society's Significance magazine, estimated that there were closer to 2 million rats in the city. 

Rats have an extremely high rate of reproduction, mating up to 20 times in 6 hours. A female rat
produces 4–7 litters of around 10 rats each year. Studies indicate New York is particularly well-suited for rats due to sanitation practices, climate, housing construction standards and more. Warmer weather due to climate change makes for longer mating seasons and an increase in rat populations. """
)

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
trash_url = "https://raw.githubusercontent.com/CMU-IDS-2020/a3-puppy-patrol/master/DSNY_Monthly_Tonnage_Data.csv"

df = pd.read_csv(rats_url)

instructions(
    "Brush across the timeline to see how rat sightings are distributed around New York City over time."
)
st.write(
    """
<iframe width="100%" height="849" frameborder="0"
  src="https://observablehq.com/embed/d86f0aead751903e?cell=chart"></iframe>
""",
    unsafe_allow_html=True,
)

st.write(
    """
Rats primarily find food at human habitations, such as in the trash. A contributing factor to the rat population is how the city collects trash: bags are left outside overnight before pick up the next morning.

> “It’s just an all-night buffet for the rats,” Jason Munshi-South, a biology professor at Fordham University said. 

"""
)

df_trash = pd.read_csv(trash_url).groupby("BOROUGH").sum().reset_index()
# df_trash = df_trash.groupby("BOROUGH").count().reset_index()
# chart = (
#    alt.Chart(nyc_geojson)
#    .mark_geoshape(color="count(BOROUGH):Q")
#    .transform_lookup(
#        lookup="BOROUGH", from_=alt.LookupData(trash_url, key="BOROUGH")
#    )
# )
# st.write(chart)

h2("How NYC Combats the Rat Population")
st.markdown(
    """
    Commonly NYC gov and exterminator suggested maintenance measures: 
- Rodent baiting
- Proper storage of garbage
- Removal of water sources
- Elimination of environments suitable for nesting
- Metal garbage cans rather than plastic ones
- Garbage should be placed out on the street close to the pickup time, rather than the night before.
- Landscaped areas around property should be kept free of tall weeds and trim shrubs that are close to the ground.
- Fix cracks or holes in the foundation of your building.
- Do not litter and do not feed birds or other wildlife.
- Call 311 or fill out NYC Rat Sighting Report online, which are are investigated by the Health Department.

The New York City Department of Health handles enforcement of rat infestation problems in New York City. Even those tasked with killing rats recognize they will never be eliminated. The approach has traditionally been reactive: after receiving complaints of infestation, officials would place rodent poison, traps, or contraceptives. In recent years, the city has adopted a more proactive approach to rodent control known as integrated pest management, which focuses on preventive measures. Here are a few existing ongoing legal measures:

- Under the city’s building code, developers are required to hire a licensed exterminator for any site where a building is being demolished. But there is no similar rule for new developments.
- Property owners that fail inspections receive a Commissioner's Order and have five days to correct the problem. If, after five days, the property fails a second inspection, the owner receives a Notice of Violation and can be fined. 
- Waste management in problem neighborhoods and buildings, 
- New York City publishes a guide for property owners and tenants, entitled Preventing Rats on Your Property: A Guide for Property Owners and Tenants 
"""
)

df_budget_raw = pd.read_csv(budget_url)
df_budget = df_budget_raw.groupby("Fiscal Year").mean().reset_index()
df_budget["year"] = df_budget["Fiscal Year"].apply(lambda d: f"{d}-01-01")
chw = 275

chart = (
    (
        alt.Chart(nyc_geojson)
        .mark_geoshape()
        .encode(color="REFUSETONSCOLLECTED:Q", tooltip="properties.boro_name:N")
    )
    .transform_lookup(
        lookup="properties.boro_name",
        from_=alt.LookupData(
            df_trash, key="BOROUGH", fields=["REFUSETONSCOLLECTED", "BOROUGH"]
        ),
    )
    .properties(width=640)
)
st.write(chart)


h2("Solution?")
st.write(
    """
How NYC Combats the Rat Population

Commonly NYC gov and exterminator suggested maintenance measures: 
* Rodent baiting
* Proper storage of garbage
* Removal of water sources
* Elimination of environments suitable for nesting
* Garbage cans need to be rat-resistant and made out of metal rather than plastic which rats easily chew through plastic, 
* Garbage should be placed out on the street close to the pickup time, rather than the night before.
* Landscaped areas around property should be kept free of tall weeds and trim shrubs that are close to the ground.
* Check for cracks or holes in the foundation of your building, sidewalk and under doors and repair them by filling and sealing them.
* Do not litter and do not feed birds or other wildlife.
* Call 311 or fill out NYC Rat Sighting Report online, which are are investigated by the Health Department.

The New York City Department of Health handles enforcement of rat infestation problems in New York City. Even those tasked with killing rats recognize they will never be eliminated. The approach has traditionally been reactive: after receiving complaints of infestation, officials would place rodent poison, traps, or contraceptives. In recent years, the city has adopted a more proactive approach to rodent control known as integrated pest management, which focuses on preventive measures. Here are a few existing ongoing legal measures:

* Under the city’s building code, developers are required to hire a licensed exterminator for any site where a building is being demolished. But there is no similar rule for new developments.
* Property owners that fail inspections receive a Commissioner's Order and have five days to correct the problem. If, after five days, the property fails a second inspection, the owner receives a Notice of Violation and can be fined. 
* Waste management in problem neighborhoods and buildings, 
* New York City publishes a guide for property owners and tenants, entitled Preventing Rats on Your Property: A Guide for Property Owners and Tenants

Mayors will often wage a “war on rats” and occasionally enact more drastic policy measures. Some of these efforts can be seen in this visualization below.

"""
)

instructions("Hover over a dot to see the policy and it's description!")

st.write(
    """
    <iframe width="100%" height="584" frameborder="0"
  src="https://observablehq.com/embed/134b3d0b7270b3c5?cell=chart"></iframe>
""",
    unsafe_allow_html=True,
)

st.write(
    """
* Working: $32 million allocation in 2017 is WORKING
    * Covering dirt floors at scores of public housing buildings
    * Deploying 336 new rat-proof garbage bins that compact trash using solar power and cost $7,000 a piece. 
    * It also calls for the City Council to pass legislation requiring medium and large buildings in the targeted areas to put out their trash for pickup early in the morning, ridding sidewalks of the overnight trash mounds that attract vermin.
    * And it includes a new process to kill rats in their burrows using dry ice, a method only recently approved by the Environmental Protection Agency and tested to promising effect in some areas of the city last year.
* Working: Rat reservoir program - more inspections
* What’s not working: birth control for rats (Rats are hard to kill. They avoid new objects introduced to their environment. They generally avoid traps and can smell poison, avoiding bait unless other food sources are unavailable.)
* What’s not working: Cats (rats simply avoid cats, and cats are inclined to attack easier prey like birds)

Suggestions tldr: keep doing what you’re doing - increase sanitation and inspections 
"""
)

st.write(
    "Mayors will often wage a “war on rats” and occasionally enact more drastic policy measures."
)
instructions("Some of these efforts can be seen in this visualization below.")


st.markdown(
    """
<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-h395{background-color:#ffeceb;text-align:left;vertical-align:top}
.tg .tg-y4nm{background-color:#efffef;text-align:left;vertical-align:top}
.tg .tg-0lax{text-align:left;vertical-align:top}
</style>
<table class="tg" style="undefined;table-layout: fixed; width: 679px">
<colgroup>
<col style="width: 320px">
<col style="width: 359px">
</colgroup>
<thead>
  <tr>
    <th class="tg-y4nm"><span style="font-weight:bold;color:#009901">What's working 👍</span></th>
    <th class="tg-h395"><span style="font-weight:bold;color:#9A0000">What's not working  👎</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax">De Blasio's $32 million plan in 2017 that involved better garbage bins, <span style="font-weight:400;font-style:normal;text-decoration:none">covering dirt floors at public housing buildings, and introducing dry ice as a new way to kill rats. Our visualizations support this: at the beginning of this policy, our graph shows a strong decline in rat sightings.</span></td>
    <td class="tg-0lax">Cats. Although some suggest introducing cats as a counterbalance to rats, 2018 research finds that contrary to popular opinion, cats are not good predators of rats. Rats actively avoid cats, and the researchers only recorded two rat kills in 79 days. The findings add to growing evidence that any benefit of using cats to control city rats is outweighed by the threat they pose to birds and other urban wildlife.</td>
  </tr>
  <tr>
    <td class="tg-0lax">The 2014 Rodent Reservoir Analysis program. Inspectors set bait for the rats, closed burrows, flushed sewers, and worked with the neighboring community on best practices, such as better trash management programs. Based on reports, the program has led to an 80% to 90% reduction in rodent sightings in the neighborhoods involved in the initiative.</td>
    <td class="tg-0lax"><span style="font-weight:400;font-style:normal">The 2013 plan for mass sterilization of the city's rats, using a chemical to neutralize the reproductive systems of female rats. T</span><span style="font-weight:400;font-style:normal;text-decoration:none">his program was unsuccessful because rats avoid new objects introduced to their environment. They generally avoid traps and can smell poison, avoiding bait unless other food sources are unavailable.</span></td>
  </tr>
</tbody>
</table>
""",
    unsafe_allow_html=True,
)

h3("End Summary")

st.markdown(
    """
The data shows that NYC residents find dark humor in the prevalence of and size of rats but would love to see them gone. The problem is widespread all across the city, but trends towards Brooklen and Manhattan, which are also hotspots for trash output. 

However, optimistically, the data shows that De Blasio's $32 million plan is correlated with a decrease in rat sightings! NYC should keep doing what it's been doing in the past few years.

Although rats have become part of the fabric of NYC’s environment and have unprecedented levels of internet fame, most New Yorkers would be glad to see them go. However, this is still an ongoing war with no end in sight, and rats are a formidable enemy.

> “It’s a never-ending battle, but it’s the right thing to do,” said Joseph J. Lhota, former deputy mayor and rat czar, “Never, never, never give up… People are disgusted by rats.”
"""
)

h3("Data sources")
st.markdown(
    """
- NYC Open Data
- Google Images and Flickr
- Reddit
- Wikipedia, New York Times, New York Pest Control, and The Guardian for information about rats
"""
)
