import argparse
import requests
import os
import sys
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "http://api.openweathermap.org/geo/1.0/"
API_KEY = os.getenv('OPENWEATHER_API_KEY')

def fetch_coordinates_by_city(city, state):
    """Fetch coordinates using city and state"""
    url = f"{BASE_URL}direct?q={city},{state},US&appid={API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data:
            return data[0]
        else:
            return None
    return None


def fetch_coordinates_by_zip(zip_code):
    """Fetch coordinates using zip code"""
    url = f"{BASE_URL}zip?zip={zip_code},US&appid={API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data:
            return data
        else:
            return None
    return None


def get_location_info(location):
    """Identify if the input is a city/state or zip code, then fetch info"""
    if location.isdigit():
        return fetch_coordinates_by_zip(location)
    elif "," in location:  
        city, state = map(str.strip, location.split(","))
        return fetch_coordinates_by_city(city, state)
    else:
        print(f"Invalid input format for location: {location}")
        return None


def main():
    if not API_KEY:
        print("Error: Missing API Key. Please set the OPENWEATHER_API_KEY environment variable.")
        sys.exit(1)

    parser = argparse.ArgumentParser(description="Fetch latitude and longitude using OpenWeather Geocoding API.")
    parser.add_argument('locations', nargs='+', help="List of locations (city/state or zip code)")

    args = parser.parse_args()

    for location in args.locations:
        result = get_location_info(location)
        if result:
            print(f"Location: {result.get('name', 'N/A')}, Lat: {result.get('lat', 'N/A')}, Lon: {result.get('lon', 'N/A')}")
        else:
            print(f"Could not find location for {location}")


if __name__ == "__main__":
    main()