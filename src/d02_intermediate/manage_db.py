import sqlite3

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


def insert_data():
    with sqlite3.connect("data/02_intermediate/main.db") as conn:
        c = conn.cursor()
        c.execute(cmd)
        conn.commit()
