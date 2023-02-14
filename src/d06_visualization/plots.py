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
