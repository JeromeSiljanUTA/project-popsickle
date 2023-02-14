"""
This module calls other modules to clean and display our data and predictions
"""
from d01_data.get_weather import get_weather_city
from d01_data.load_data import import_files, load_from_db
from d02_intermediate.manage_db import insert_power_data, insert_weather_data
from d06_visualization.plots import plot_weather

POWER_DATA_POPULATED = True
WEATHER_DATA_POPULATED = True

POWER_DATA = 1
WEATHER_DATA = 2

if not POWER_DATA_POPULATED:
    df = import_files()
    insert_power_data(df)

if not WEATHER_DATA_POPULATED:
    df = get_weather_city()
    insert_weather_data(df)

power_df = load_from_db(POWER_DATA)
weather_df = load_from_db(WEATHER_DATA)
