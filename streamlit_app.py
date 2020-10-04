import streamlit as st
import pandas as pd
import altair as alt

st.title("""
        # Aww Rats!🐀
        An exploration of rat sightings in New York City, courtesy of [NYC Open Data](https://data.cityofnewyork.us/Social-Services/Rat-Sightings/3q43-55fe).
        """)

geojson_url = "https://raw.githubusercontent.com/CMU-IDS-2020/a3-puppy-patrol/master/2010_Census_Blocks.geojson" 
geojson = alt.Data(url=geojson_url, format=alt.DataFormat(property='features', type='json'))

rats_url = "https://raw.githubusercontent.com/CMU-IDS-2020/a3-puppy-patrol/master/rats.csv"

gm = alt.Chart(geojson).mark_geoshape(fill="none", stroke="black", strokeWidth=0.05)

map = alt.Chart(rats_url).mark_circle(size=3.0, opacity=0.05).encode(
        longitude="Longitude:Q",
        latitude="Latitude:Q",
        color="Borough:N"
).transform_filter("datum.Longitude > -75")
st.write(gm + map)


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
        x=alt.X("Created Date:T",
            timeUnit="year"),
        y=alt.Y("Created Date:T",
            aggregate="count",
            timeUnit="year")
)
st.write(chart)
