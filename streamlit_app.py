import streamlit as st
import pandas as pd
import altair as alt
import pydeck as pdk

st.title(
    """
        # Aww Rats!🐀
        ## Who Runs New York?
        Rats are as synonymous with New York City as trains, the Empire State Building, and expensive apartments. There is even a [Wikipedia page dedicated to Rats in New York City](https://en.wikipedia.org/wiki/Rats_in_New_York_City). While cute and furry creatures, rats are also disease vectors (not that we need more of those right now). The City even went so far as to make a [$32 million plan](https://www.nytimes.com/2017/07/12/nyregion/new-york-city-rat-problem.html) to control the rodent problem.
        According to [NYC Open Data](https://data.cityofnewyork.us/Social-Services/Rat-Sightings/3q43-55fe) the number of reports of rat sightings has been on an upward trend.
        """
)

# Using URLs for df > 5k rows

rats_url = (
    "https://raw.githubusercontent.com/CMU-IDS-2020/a3-puppy-patrol/master/rats.csv"
)


df = pd.read_csv("rats.csv")
df = df[df["longitude"] > -75]
years = df["created_date"].apply(lambda x: x[6:10]).unique()
years = [int(year) for year in years]
min_year = min(years)
max_year = max(years)
select_year = st.slider("Year", min_year, max_year)

st.write()

st.map(df[df["created_date"].apply(lambda x: int(x[6:10])) == select_year])

chart = (
    alt.Chart(rats_url)
    .mark_line()
    .encode(
        x=alt.X("created_date:T", timeUnit="year", title="Complaint Creation Date"),
        y=alt.Y("count(unique_key):Q", title="Count of Complaints"),
    )
    .properties(width=700)
)
st.write(chart)


st.write("Lets look at the number of days a request is open")
open_mean = df.groupby(["borough"])["days_open"].mean().reset_index()
chart = (
    alt.Chart(open_mean)
    .mark_bar()
    .encode(x="days_open:Q", y="borough:N")
    .transform_filter("datum.borough !== 'Unspecified'")
)
st.write(chart)

chart = alt.Chart(rats_url).mark_bar().encode(x="borough:N", y="count(borough):Q")
st.write(chart)

chart = alt.Chart(rats_url).mark_rect(opacity=0.025).encode(x="borough:N", y="status:N")
st.write(chart)

chart = (
    alt.Chart(rats_url)
    .mark_rect(opacity=0.25)
    .encode(x=alt.X("created_date:T", timeUnit="hours"), y="borough:N")
)

st.write(chart)
