"""
Moves intermediate DataFrame into SQLite3 database
"""

import sqlite3

CREATE_TABLE = """
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
INSERT_INTO = """
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


def insert_data(df):
    """
    Adds Excel data to SQLite3 database,
    creates table if one does not already exist
    """
    with sqlite3.connect("data/02_intermediate/main.db") as conn:
        cursor = conn.cursor()
        cursor.execute(CREATE_TABLE)
        for row in df.iterrows():
            row = row[1]
            cursor.execute(
                f"""
                {INSERT_INTO}"{row[0]}", "{row[1]}", "{row[2]}", "{row[3]}", "{row[4]}", "{row[5]}", "{row[6]}", "{row[7]}", "{row[8]}", "{row[9]}")
                """
            )

        conn.commit()
