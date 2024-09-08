import requests
import json
import os
import collections

weather = collections.namedtuple('weather', 'description wind_speed temp unit')


def read_json_config():
    """
    Read JSON configuration file and store the data.
    """

    file_path = os.path.abspath(os.path.join('.', 'Resources', 'config' + '.json'))

    with open(file_path, 'r') as file:
        config_data = json.load(file)
    return config_data


def get_weather_data(location):
    print("-------------------------------------------------------------------------------------")
    print()
    print(f"Getting Weather details for {location.city}, {location.country}")
    print()
    print("-------------------------------------------------------------------------------------")

    url = get_url(location)
    request = requests.get(url)

    if request.status_code in (400, 404, 500):
        print(f"Error {request.text}")

    data = request.json()

    description = ""
    wind_speed = ""
    temp = ""
    unit = "C"

    if data['units'] == 'imperial':
        unit = 'F'

    description = data.get("weather").get("description")
    wind_speed = data.get("wind").get("speed")
    temp = data.get("forecast").get("temp")


    return weather(description, wind_speed, temp, unit)


def get_url(location):
    url_str = f'https://weather.talkpython.fm/api/weather?city={location.city}'
    config_data = read_json_config()
    if location.state:
        url_str += f'&state={location.state}&country={location.country}'
    else:
        url_str += f'&country={location.country}'

    if location.city in config_data:
        url_str += f'&units={config_data.get(location.city).get("units")}'

    return url_str
