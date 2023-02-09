import requests

coordinate_dictionary = {
    "North": {"Lubbock": "", "Wichita Falls": ""},
    "Far West": {"Midland": ""},
    "West": {"Abilene": ""},
    "South": {"Corpus Christi": "", "MC Allen": "", "Brownsville": ""},
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

    return coordinate_dictionary


# "http://api.openweathermap.org/geo/1.0/direct?q=Dallas,Texas&limit=5&appid=b00f34717fba5600775435f8e4be44bb"
# - https://open-meteo.com/en/docs/historical-weather-api#latitude=32.78&longitude=-96.81&start_date=2002-01-01&end_date=2022-12-31&hourly=temperature_2m
# - https://openweathermap.org/api/geocoding-api
