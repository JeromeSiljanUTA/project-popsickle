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
    "ERCOT" TEXT,
"""
INSERT_INTO = """
INSERT INTO power_draw(
    Hour_Ending,
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


def insert_data():
    """
    Adds Excel data to SQLite3 database,
    creates table if one does not already exist
    """
    with sqlite3.connect("data/02_intermediate/main.db") as conn:
        cursor = conn.cursor()
        cursor.execute(CREATE_TABLE)
        conn.commit()
