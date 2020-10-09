import streamlit as st
import pandas as pd
import altair as alt

st.title("""
        # Aww Rats!🐀
        An exploration of rat sightings in New York City, courtesy of [NYC Open Data](https://data.cityofnewyork.us/Social-Services/Rat-Sightings/3q43-55fe).
        """)

# Using URLs for df > 5k rows

rats_url = "https://raw.githubusercontent.com/CMU-IDS-2020/a3-puppy-patrol/master/rats.csv"
df = pd.read_csv("rats.csv")

st.map(df) 


chart = alt.Chart(rats_url).mark_bar().encode(
        x="borough:N",
        y="count(borough):Q"
)
st.write(chart)

chart = alt.Chart(rats_url).mark_rect(opacity=0.025).encode(
        x="borough:N",
        y="status:N"
        )
st.write(chart)

chart = alt.Chart(rats_url).mark_line().encode(
        x=alt.X("created_date:T",
            timeUnit="year"),
        y=alt.Y("created_date:T",
            aggregate="count",
            timeUnit="year")
)
st.write(chart)

chart = alt.Chart(rats_url).mark_rect(opacity=0.25).encode(
        x=alt.X("created_date:T", timeUnit="hours"),
        y="borough:N"
)

st.write(chart)
