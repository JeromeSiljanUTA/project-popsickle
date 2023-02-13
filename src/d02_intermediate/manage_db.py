"""
Moves intermediate DataFrame into SQLite3 database
"""

import sqlite3
import os

CREATE_POWER_DRAW_TABLE = """
CREATE TABLE IF NOT EXISTS power_draw(
    "Hour Ending" TEXT,
    "COAST" TEXT,
    "EAST" TEXT,
    "FWEST" TEXT,
    "NORTH" TEXT,
    "NCENT" TEXT,
    "SOUTH" TEXT,
    "SCENT" TEXT,
    "WEST" TEXT,
    "ERCOT" TEXT
)
"""
CREATE_WEATHER_TABLE = """
CREATE TABLE IF NOT EXISTS weather(
    "Time" TEXT,
    "Tempterature" REAL,
    "Region" TEXT,
    "City" TEXT
)
"""
INSERT_INTO_POWER_DRAW = """
INSERT INTO power_draw(
    "Hour Ending",
    COAST,
    EAST,
    FWEST,
    NORTH,
    NCENT,
    SOUTH,
    SCENT,
    WEST,
    ERCOT) 
    VALUES(
"""
INSERT_INTO_WEATHER = """
INSERT INTO weather(
    Time,
    Temperature,
    Region,
    City)
    VALUES(
"""


def insert_power_data(df):
    """
    Adds Excel data to SQLite3 database,
    creates table if one does not already exist
    """
    if not os.path.isdir("data/02_intermediate"):
        os.mkdir("data/02_intermediate")
    with sqlite3.connect("data/02_intermediate/main.db") as conn:
        cursor = conn.cursor()
        cursor.execute(CREATE_WEATHER_TABLE)
        for row in df.iterrows():
            row = row[1]
            cursor.execute(
                f"""
                {INSERT_INTO_POWER_DRAW}"{row[0]}", "{row[1]}", "{row[2]}", "{row[3]}", "{row[4]}", "{row[5]}", "{row[6]}", "{row[7]}", "{row[8]}", "{row[9]}")
                """
            )
        conn.commit()


def insert_weather_data(df):
    if not os.path.isdir("data/02_intermediate"):
        os.mkdir("data/02_intermediate")
    with sqlite3.connect("data/02_intermediate/main.db") as conn:
        cursor = conn.cursor()
        cursor.execute(CREATE_WEATHER_TABLE)
        for row in df.iterrows():
            row = row[1]
            cursor.execute(
                f"""
                {INSERT_INTO_WEATHER}"{row[0]}", "{row[1]}", "{row[2]}", "{row[3]}")
                """
            )
        conn.commit()
