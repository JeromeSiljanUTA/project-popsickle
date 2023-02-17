import logging

import pandas as pd
import requests

# holds regions, cities, and is later populated with the coordinates
# of the cities
coordinate_dictionary = {
    "North": {"Lubbock": "", "Wichita Falls": ""},
    "Far West": {"Midland": ""},
    "West": {"Abilene": ""},
    "South": {"Corpus Christi": "", "MCAllen": "", "Brownsville": ""},
    "South Central": {"Austin": "", "San Antonio": ""},
    "North Central": {"Dallas": "", "Fort Worth": ""},
    "East": {"Tyler": ""},
    "Coast": {"Houston": ""},
}


def get_coordinates(city_name):
    """
    Args:
        city_name: name of city

    Returns:
        tuple of latitide and longitude of city
        -1 if failed
    """
    try:
        response = requests.get(
            f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},Texas&limit=5&appid=b00f34717fba5600775435f8e4be44bb"
        ).json()[0]

        return (response["lat"], response["lon"])
    except:
        return -1


def populate_coordinate_dictionary():
    """
    populates coordinate dictionary for every city in every region
    """
    for region in coordinate_dictionary.values():
        for city in region:
            region[city] = get_coordinates(city)


def get_weather_city():
    """
    gathers weather data from API and populates dataframe
    Returns: dataframe of hourly data for every city
    """
    # add coordinates to dictionary
    populate_coordinate_dictionary()
    data_list = []
    for region_dict, region in zip(
        coordinate_dictionary.values(), coordinate_dictionary.keys()
    ):
        for city in region_dict:
            coords = region_dict[city]
            if isinstance(coords, tuple):  # checking if failed to get coordinates
                response = requests.get(
                    f"https://archive-api.open-meteo.com/v1/archive?latitude={coords[0]}&longitude={coords[1]}&start_date=2002-01-01&end_date=2022-12-31&hourly=temperature_2m&timezone=America%2FChicago&temperature_unit=fahrenheit",
                    timeout=15,
                )
                df = pd.DataFrame.from_dict(response.json()["hourly"])
                df["time"] = pd.to_datetime(df["time"])
                df["Region"] = region
                df["City"] = city
                data_list.append(df)
            else:
                logging.error("%s did not get coordinates", city)
    return pd.concat(data_list)
