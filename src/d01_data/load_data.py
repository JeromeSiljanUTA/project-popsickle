"""
Loads data from CSV into DataFrame
"""
import sqlite3
from enum import Enum

import pandas as pd
from d02_intermediate.fix_date import clean_df

rename_dict = {
    "HourEnding": "Hour Ending",
    "Hour_End": "Hour Ending",
    "FAR_WEST": "FWEST",
    "NORTH_C": "NCENT",
    "SOUTHERN": "SOUTH",
    "SOUTH_C": "SCENT",
}

file_list = [
    "2003_ercot_hourly_load_data.xls",
    "2004_ercot_hourly_load_data.xls",
    "2005_ercot_hourly_load_data.xls",
    "2006_ercot_hourly_load_data.xls",
    "2007_ercot_hourly_load_data.xls",
    "2008_ercot_hourly_load_data.xls",
    "2009_ercot_hourly_load_data.xls",
    "2010_ercot_hourly_load_data.xls",
    "2011_ercot_hourly_load_data.xls",
    "2012_ercot_hourly_load_data.xls",
    "2013_ercot_hourly_load_data.xls",
    "2014_ercot_hourly_load_data.xls",
    "native_load_2015.xls",
    "native_Load_2016.xlsx",
    "native_Load_2017.xlsx",
    "Native_Load_2018.xlsx",
    "Native_Load_2019.xlsx",
    "Native_Load_2020.xlsx",
    "Native_Load_2021.xlsx",
    "Native_Load_2022.xlsx",
]


def import_files():
    """
    Reads list of Excel files, renames column headers,
    and adds to DataFrame

    Returns:
        DataFrame with Excel data

    """
    for idx, file_name in enumerate(file_list):
        file_name = f"data/01_raw/{file_name}"
        if idx == 0:
            df = clean_df(pd.read_excel(file_name).rename(columns=rename_dict))
        else:
            tmp_df = clean_df(pd.read_excel(file_name).rename(columns=rename_dict))
            df = pd.concat([df, tmp_df])

    return df.reset_index().drop(columns=["index"])


def load_from_db(TABLE):
    """
    Queries SQLite3 database and populates DataFrame
    Returns:
    DataFrame from SQLite3 database

    """
    with sqlite3.connect("data/02_intermediate/main.db") as conn:
        if TABLE == 1:
            df = pd.read_sql("SELECT * FROM power_draw", conn)
        else:
            df = pd.read_sql("SELECT * FROM weather", conn)
        df["Time"] = pd.to_datetime(df["Time"])
        cols = df.columns.to_list()
        cols.remove("Time")
        try:
            cols.remove("Region")
            cols.remove("City")
            df = df.query("COAST != 'NaT'")
        except ValueError:
            pass
        for column in cols:
            df[column] = df[column].astype("float")
        return df
