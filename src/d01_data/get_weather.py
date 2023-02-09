import pandas as pd
import requests

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
    try:
        response = requests.get(
            f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},Texas&limit=5&appid=b00f34717fba5600775435f8e4be44bb"
        ).json()[0]

        return (response["lat"], response["lon"])
    except:
        return -1


def get_coordinate_dictionary():
    for region in coordinate_dictionary.values():
        for city in region:
            region[city] = get_coordinates(city)


def get_weather_city():
    data_list = []
    for region_dict, region in zip(
        coordinate_dictionary.values(), coordinate_dictionary.keys()
    ):
        for city in region_dict:
            coords = region_dict[city]
            if coords != -1:
                response = requests.get(
                    f"https://archive-api.open-meteo.com/v1/archive?latitude={coords[0]}&longitude={coords[1]}&start_date=2002-01-01&end_date=2022-12-31&hourly=temperature_2m&timezone=America%2FChicago&temperature_unit=fahrenheit"
                )
                df = pd.DataFrame.from_dict(response.json()["hourly"])
                df["time"] = pd.to_datetime(df["time"])
                df["Region"] = region
                df["City"] = city
                data_list.append(df)
            else:
                print(f"{city} did not get coordinates")
    return pd.concat(data_list)
