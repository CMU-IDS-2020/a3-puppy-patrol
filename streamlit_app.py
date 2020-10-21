import streamlit as st
import pandas as pd
import altair as alt
import pydeck as pdk
from datetime import datetime

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

# Using URLs for df > 5k rows
rats_url = (
    "https://raw.githubusercontent.com/CMU-IDS-2020/a3-puppy-patrol/master/rats.csv"
)


df = pd.read_csv("rats.csv")

boroughs = list(df["borough"].unique())
boroughs.append("ALL")
boroughs.reverse()
borough = st.radio("Select Borough", boroughs)
df_borough = df if borough == "ALL" else df[df["borough"] == borough]

chart = (
    alt.Chart(df_borough)
    .mark_line()
    .encode(
        x=alt.X("created_date:T", timeUnit="year", title="Complaint Creation Date"),
        y=alt.Y("count(unique_key):Q", title="Count of Complaints"),
    )
    .properties(width=700)
)

st.write(chart)

years = list(df["created_date"].apply(lambda d: datetime.fromisoformat(d).year))
min_year = min(years)
max_year = max(years)
select_year = st.slider("Select Year", min_year, max_year)
df_year_bool = df["created_date"].apply(
    lambda d: datetime.fromisoformat(d).year == select_year
)
df_year = df[df_year_bool]

vs = pdk.ViewState(
        latitude=df['latitude'].mean(),
        longitude=df['longitude'].mean(),
        zoom=10
        )

layer = pdk.Layer(
    "ScatterplotLayer",
    df_year[["latitude", "longitude"]],
    get_position=["longitude", "latitude"],
    auto_highlight=True,
    pickable=True,
    get_radius=100,
    get_fill_color=[255, 0, 0],
    opacity=0.05,
    filled=True,
)

st.write(pdk.Deck(layers=[layer], initial_view_state=vs))

