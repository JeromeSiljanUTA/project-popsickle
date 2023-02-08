"""
This module cleans the data and puts it in an sqlite3 database
"""

import datetime as dt

import pandas as pd


def back_str_hour(date_str):
    """
    Takes a date string and subtracts one hour
    Args:
        date_str: date in string format to be manipulated

    Returns:
        string of date one hour previous

    """
    try:
        # don't go to end of string to cut out DST
        return (
            f"{date_str[:11]}{str(int(date_str[11:13]) - 1).zfill(2)}{date_str[13:16]}"
        )
    # one line is formatted as datetime and not string
    except TypeError:
        return str(date_str - dt.timedelta(hours=1))


def clean_df(df):
    """
    Formats column as datetime by subtracting one
    hour as a string, converting to datetime, and
    adding an hour. This is done to change the 01:24
    hour format to 00:23

    Returns:
        DataFrame with the "Hour Ending" column as
        datetime.

    """
    df["Hour Ending"] = df["Hour Ending"].apply(back_str_hour)
    df["Hour Ending"] = pd.to_datetime(df["Hour Ending"]) + dt.timedelta(hours=1)
    return df
