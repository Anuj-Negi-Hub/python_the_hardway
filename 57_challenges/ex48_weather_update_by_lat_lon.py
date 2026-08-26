'''
Using the OpenWeatherMap API at http://openweathermap.org/ current, create a program that prompts for a city name and
returns the current temperature for the city.

Example Output
Where are you? Chicago IL
Chicago weather:
65 degrees Fahrenheit
'''

import requests


api_key = "295d9d6c85a7f2922f813e39a2dd2a0a"
url = "http://api.openweathermap.org/geo/1.0/zip"
country_code = input("Type the coundry code a per ISO 3166: ")
zip_code = input("Type the zip code of the place you want to know the temperature: ")

# zip_country_code = "zip_code, country_code"

#require zip code and cuntry code to fetch the laitude and longitude
params = {
    "zip": f"{zip_code},{country_code}", #use comma without space to seperate the zip code and country code
    "appid": api_key
}


response = requests.get(url, params=params)
#convert json data to python object
data = response.json()

lat = data["lat"]
lon = data["lon"]
# print(lat)
# print(lon)

# as now we have lat and lon of the state/city, we can now use the lat&lon API to fetech the temperature of the city/state

new_url = "https://api.openweathermap.org/data/2.5/weather" # ?lat=44.34&lon=10.99&appid={API key}

new_params = {
    "lat": lat,
    "lon": lon,
    "appid": api_key,
    "units": "metric"
}

new_response = requests.get(new_url, params=new_params)
new_data = new_response.json()
# print(new_data)

# as we now have the data, we can get the temperature of the city

current_temp = new_data['main']['temp']
print(current_temp)  