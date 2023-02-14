import datetime as dt

import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import seaborn as sns


def plot_weather(df, city=None, region=None, year=None):
    if region is not None:
        if isinstance(region, list):
            df = df[df["Region"].isin(region)]
        else:
            df = df[df["Region"] == region]
    if year is not None:
        if isinstance(year, list):
            df = df[df["Time"].dt.year.isin(year)]
        else:
            df = df[df["Time"].dt.year == year]
    if city is not None:
        if isinstance(city, list):
            df = df[df["City"].isin(city)]
        else:
            df = df[df["City"] == city]

    fig = px.line(df, x="Time", y="Temperature", color="City")
    fig.show()
