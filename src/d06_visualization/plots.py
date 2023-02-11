import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import seaborn as sns


def plotly_weather(weather_df):
    weather_gb = weather_df.groupby("City")
