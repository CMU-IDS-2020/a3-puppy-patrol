import streamlit as st
import pandas as pd
import altair as alt

st.title("""
        # Aww Rats!🐀
        An exploration of rat sightings in New York City, courtesy of [NYC Open Data](https://data.cityofnewyork.us/Social-Services/Rat-Sightings/3q43-55fe).
        """)

rats_url = "https://raw.githubusercontent.com/CMU-IDS-2020/a3-puppy-patrol/master/rats.csv"

map = alt.Chart(rats_url).mark_circle(opacity=0.05).encode(
        longitude="Longitude:Q",
        latitude="Latitude:Q",
        color="Borough:N"
).transform_filter("datum.Longitude > -75")
st.write(map)


chart = alt.Chart(rats_url).mark_bar().encode(
        x="Borough:N",
        y="count(Borough):Q"
)
st.write(chart)

chart = alt.Chart(rats_url).mark_rect(opacity=0.05).encode(
        x="Borough:N",
        y="Status:N"
)
st.write(chart)

chart = alt.Chart(rats_url).mark_line().encode(
        x="created_date:O",
        y="count(created_date):Q"
)

st.write(chart)

st.write(pd.read_csv(rats_url))
