"""
This module cleans the data and puts it in an sqlite3 database
"""

import datetime as dt
import sqlite3

import pandas as pd

cmd = """
CREATE TABLE IF NOT EXISTS power_draw(
    "Hour_Ending" TEXT,
    "COAST" TEXT,
    "EAST" TEXT,
    "FWEST" TEXT,
    "NORTH" TEXT,
    "NCENT" TEXT,
    "SOUTH" TEXT,
    "SCENT" TEXT,
    "WEST" TEXT,
    "ERCOT" TEXT,
    PRIMARY KEY(Hour_Ending))
"""


def back_str_hour(date_str):
    try:
        # don't go to end of string to cut out DST
        return (
            f"{date_str[:11]}{str(int(date_str[11:13]) - 1).zfill(2)}{date_str[13:16]}"
        )
    # one line is formatted as datetime and not string
    except TypeError:
        return str(date_str - dt.timedelta(hours=1))


def clean_df(df):
    df["Hour Ending"] = df["Hour Ending"].apply(back_str_hour)
    df["Hour Ending"] = pd.to_datetime(df["Hour Ending"]) + dt.timedelta(hours=1)
    return df


def import_files():
    for idx, file_name in enumerate(file_list):
        file_name = f"data/01_raw/{file_name}"
        if idx == 0:
            df = clean_df(pd.read_excel(file_name).rename(columns=rename_dict))
        else:
            tmp_df = clean_df(pd.read_excel(file_name).rename(columns=rename_dict))
            df = pd.concat([df, tmp_df])

    return df.reset_index().drop(columns=["index"])


with sqlite3.connect("data/main.db") as conn:
    c = conn.cursor()
    c.execute(cmd)
    conn.commit()
