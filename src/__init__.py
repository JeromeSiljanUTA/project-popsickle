"""
This module calls other modules to clean and display our data and predictions
"""
import argparse
import logging

from d01_data.get_weather import get_weather_city
from d01_data.load_data import import_files, load_from_db
from d02_intermediate.manage_db import insert_power_data, insert_weather_data
from d03_processing.df_subset import get_subset
from d04_modelling.arima import fit_arima, threaded_arima
from d04_modelling.sarimax import fit_sarimax
from d06_visualization.plots import plot_power, plot_weather

# Initialize argparse parser
parser = argparse.ArgumentParser()
parser.add_argument(
    "--insert",
    help="insert values to database, run on the first time",
    action="store_true",
)

args = parser.parse_args()

# Initialize logging object
log = logging.getLogger(__name__)

# Populate database if insert option was set
if args.insert:
    POWER_DATA_POPULATED = False
    WEATHER_DATA_POPULATED = False
else:
    POWER_DATA_POPULATED = True
    WEATHER_DATA_POPULATED = True

POWER_DATA = 1
WEATHER_DATA = 2

if not POWER_DATA_POPULATED:
    df = import_files()
    insert_power_data(df)

if not WEATHER_DATA_POPULATED:
    try:
        df = get_weather_city()
        insert_weather_data(df)
    except ValueError:
        log.error("Unable to retrieve any weather data")

power_df = load_from_db(POWER_DATA)
weather_df = load_from_db(WEATHER_DATA)


def train_arimas():
    orders = [(24, 0, 1), (24, 1, 1)]
    threaded_arima(power_df, orders)


def train_sarimax():
    seasonal_order = (4, 0, 1, 24)
    order = (0, 1, 0)
    fit_sarimax(power_df, seasonal_order, order)
