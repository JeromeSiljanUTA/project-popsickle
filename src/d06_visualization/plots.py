import datetime as dt

import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import seaborn as sns


def weather_region_year(df, region, year):
    region_df = df[df["Region"] == region]
    year_df = region_df[region_df["Time"].dt.year == year]
    fig = px.line(year_df, x="Time", y="Temperature", color="City")
    fig.show()
