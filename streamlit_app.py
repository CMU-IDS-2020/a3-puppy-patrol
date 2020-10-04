import streamlit as st
import pandas as pd
import altair as alt

st.title("""
        # Aww Rats!🐀
        An exploration of rat sightings in New York City, courtesy of [NYC Open Data](https://data.cityofnewyork.us/Social-Services/Rat-Sightings/3q43-55fe).
        """)

@st.cache  # add caching so we load the data only once
def load_data():
    filepath = "rats.csv"
    return pd.read_csv(filepath)

df = load_data()

st.write("Let's look at raw data in the Pandas Data Frame.")

#st.write(df)

#chart = alt.Chart(df).mark_point().encode(
#    x=alt.X("body_mass_g", scale=alt.Scale(zero=False)),
#    y=alt.Y("flipper_length_mm", scale=alt.Scale(zero=False)),
#    color=alt.Y("species")
#).properties(
#    width=600, height=400
#).interactive()
#
#st.write(chart)

#chart = alt.Chart(df, width=800, height=600).mark_circle(size=0.1, opacity=0.25).encode(
#        longitude="Longitude:Q",
#        latitude="Latitude:Q",
#        color="Address Type:N",
#).transform_filter("datum.Longitude > -74")
#
#st.write(chart)

bar = alt.Chart(df).mark_bar().encode(
        x="Borough:N",
        y="count(City)"
)

st.write(bar)

df.columns
