"""
This module calls other modules to clean and display our data and predictions
"""
from d01_data.load_data import import_files, load_from_db
from d02_intermediate.manage_db import insert_data

DB_POPULATED = True

if DB_POPULATED:
    df = load_from_db()
else:
    df = import_files()
    insert_data(df)
