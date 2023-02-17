import datetime as dt

import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import seaborn as sns


def get_subset(df, city=None, region=None, year=None):
    if region is not None:
        if isinstance(region, list):
            if region[0] in df.columns:
                selection = ["Time"]
                for region in region:
                    selection.append(region)
                df = df[region]
            else:
                df = df[df["Region"].isin(region)]
        else:
            if region in df.columns:
                df = df[["Time", region]]
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

    return df
