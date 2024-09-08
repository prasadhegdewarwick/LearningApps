import collections
import sys
from Resources import weather


Location = collections.namedtuple('Location', 'city state country')


def get_location():
    location = input("Where do you want the weather report (e.g. Portland, US)? ")
    loc = convert_plaintext_location(location)
    if not loc:
        while not location:
            print("Please Enter city name to get weather")
            location = input("Where do you want the weather report (e.g. Portland, US)? ")
            if location:
                loc = convert_plaintext_location(location)

    data = weather.get_weather_data(loc)
    if data:
        print_weather(data, loc)




def convert_plaintext_location(location):
    if not location:
        return None
    location_text = location.lower().strip()
    parts = location_text.split(",")
    parts = [ele.strip() for ele in parts]
    country = 'us'
    city = ""
    state = ""

    if len(parts) == 3:
        city = parts[0]
        state = parts[1][:2]
        country = parts[2][:2]
    elif len(parts) == 2:
        city = parts[0]
        country = parts[1][:2]
    elif len(parts) == 1:
        city = parts[0]
    else:
        return None

    return Location(city, state, country)


def print_weather(data, location):
    print(f" Please Find the Weather Report for {location.city} , {location.country}")
    print()
    print(f" Weather Description : {data.description}")
    print(f" Today's Temperature : {data.temp} {data.unit}")
    print(f" Wind Speed : {data.wind_speed}")

