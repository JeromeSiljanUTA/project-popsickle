import datetime as dt

import numpy as np
import pandas as pd
import plotly.express as px
from d03_processing.df_subset import get_subset


def plot_weather(df, city=None, region=None, year=None):
    """
    Plots weather data
    Args:
        df: dataframe to plot
        city: (optional) select rows with this city(s)
        region: (optional) select rows with this region(s)
        year: (optional) select rows within this year(s)

    """
    df = get_subset(df, city, region, year)
    fig = px.line(df, x="Time", y="Temperature", color="City")
    fig.show()


def plot_power(df, city=None, region=None, year=None):
    """
    Plots power data
    Args:
        df: dataframe to plot
        city: (optional) select rows with this city(s)
        region: (optional) select rows with this region(s)
        year: (optional) select rows within this year(s)

    """
    df = get_subset(df, city, region, year)
    y_list = df.columns.to_list()
    # Make sure Time is not plotted on the y axis
    y_list.remove("Time")
    fig = px.line(df, x="Time", y=y_list)
    fig.show()


def plot_daily_autocorr_power(df):
    """
    Plots daily autocorrelation data for the ERCOT column power_df
    Args:
        df: dataframe to plot
    """
    autocorr = [df["ERCOT"].autocorr(n) for n in range(0, 48)]
    fig = px.line(x=range(0, 48), y=autocorr)
    fig.show()


def plot_weekly_autocorr_power(df):
    """
    Plots weekly autocorrelation data for the ERCOT column power_df
    Args:
        df: dataframe to plot
    """
    x = np.arange(0, 8736, 52)  # checks once a week
    autocorr = [df["ERCOT"].autocorr(x_i) for x_i in x]
    fig = px.line(x=x, y=autocorr)
    fig.show()
