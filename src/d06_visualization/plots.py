import datetime as dt

import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import seaborn as sns
from d03_processing.df_subset import get_subset


def plot_weather(df, city=None, region=None, year=None):
    df = get_subset(df, city, region, year)
    fig = px.line(df, x="Time", y="Temperature", color="City")
    fig.show()


def plot_power(df, city=None, region=None, year=None):
    df = get_subset(df, city, region, year)
    y_list = df.columns.to_list()
    y_list.remove("Time")
    fig = px.line(df, x="Time", y=y_list)
    fig.show()


def plot_daily_autocorr_power(df):
    autocorr = [df["ERCOT"].autocorr(n) for n in range(0, 48)]
    fig = px.line(x=range(0, 48), y=autocorr)
    fig.show()
