"""
df_subset has a helper function that gets subsets of passed dataframes
to make plotting easier
"""
import datetime as dt

import pandas as pd


def get_subset(df, city=None, region=None, year=None):
    """
    Gets a subset of the dataframe passed
    Args:
        df: dataframe set
        city: (optional) find rows with this city(s)
        region: (optional) find rows with this region(s)
        year: (optional) find rows within this year(s)
    """
    if region is not None:
        if isinstance(region, list):
            # If a list was passed, return rows with any region in the list
            if region[0] in df.columns:
                # Add time column to list of columns to be selected
                selection = ["Time"]
                # Add regions in list to columns to be selected
                for reg in region:
                    selection.append(reg)
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
            # If a list was passed, return rows with any year in the list
            df = df[df["Time"].dt.year.isin(year)]
        else:
            df = df[df["Time"].dt.year == year]
    if city is not None:
        if isinstance(city, list):
            # If a list was passed, return rows with any city in the list
            df = df[df["City"].isin(city)]
        else:
            df = df[df["City"] == city]

    return df
