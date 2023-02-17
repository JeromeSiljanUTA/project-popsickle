"""
Moves intermediate DataFrame into SQLite3 database
"""

import logging
import os
import sqlite3

# Make sure that numerical data is stored as "real" data type
CREATE_POWER_DRAW_TABLE = """
CREATE TABLE IF NOT EXISTS power_draw(
    "Time" TEXT,
    "COAST" REAL NOT NULL CHECK(TYPEOF("COAST") == "real"),
    "EAST" REAL NOT NULL CHECK(TYPEOF("EAST") == "real"),
    "FWEST" REAL NOT NULL CHECK(TYPEOF("FWEST") == "real"),
    "NORTH" REAL NOT NULL CHECK(TYPEOF("NORTH") == "real"),
    "NCENT" REAL NOT NULL CHECK(TYPEOF("NCENT") == "real"),
    "SOUTH" REAL NOT NULL CHECK(TYPEOF("SOUTH") == "real"),
    "SCENT" REAL NOT NULL CHECK(TYPEOF("SCENT") == "real"),
    "WEST" REAL NOT NULL CHECK(TYPEOF("WEST") == "real"),
    "ERCOT" REAL NOT NULL CHECK(TYPEOF("ERCOT") == "real"),
    UNIQUE(Time)
)
"""
# Store Temperature as "real" data type
CREATE_WEATHER_TABLE = """
CREATE TABLE IF NOT EXISTS weather(
    "Time" TEXT,
    "Temperature" REAL NOT NULL CHECK(TYPEOF("Temperature") == "real"),
    "Region" TEXT,
    "City" TEXT,
    UNIQUE(Time, City)
)
"""
# Helper strings that make inserts easier and more clear
INSERT_INTO_POWER_DRAW = """
INSERT INTO power_draw(
    "Time",
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
    Args:
        df: dataframe of power data
    """
    # Create directory if it doesn't exist
    if not os.path.isdir("data/02_intermediate"):
        os.mkdir("data/02_intermediate")
    with sqlite3.connect("data/02_intermediate/main.db") as conn:
        cursor = conn.cursor()
        cursor.execute(CREATE_POWER_DRAW_TABLE)
        for row in df.iterrows():
            row = row[1]
            try:
                logging.debug(f"inserting {row} to power")
                cursor.execute(
                    f"""
                    {INSERT_INTO_POWER_DRAW}"{row[0]}", "{row[1]}", "{row[2]}", "{row[3]}", "{row[4]}", "{row[5]}", "{row[6]}", "{row[7]}", "{row[8]}", "{row[9]}")
                    """
                )
            except sqlite3.IntegrityError:
                logging.warning(f"Failed to insert {row} in power_draw table")
        conn.commit()


def insert_weather_data(df):
    if not os.path.isdir("data/02_intermediate"):
        os.mkdir("data/02_intermediate")
    with sqlite3.connect("data/02_intermediate/main.db") as conn:
        cursor = conn.cursor()
        cursor.execute(CREATE_WEATHER_TABLE)
        for row in df.iterrows():
            row = row[1]
            try:
                cursor.execute(
                    f"""
                    {INSERT_INTO_WEATHER}"{row[0]}", "{row[1]}", "{row[2]}", "{row[3]}")
                    """
                )
                print(f"inserting {row} to weather")
            except sqlite3.IntegrityError:
                logging.warning(f"Failed to insert {row} in weather table")
        conn.commit()
