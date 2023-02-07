from d01_data.load_data import import_files
from d02_intermediate.manage_db import insert_data

df = import_files()
insert_data()
