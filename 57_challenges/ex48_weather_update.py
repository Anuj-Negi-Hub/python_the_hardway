'''
Using the OpenWeatherMap API at http://openweathermap.org/ current, create a program that prompts for a city name and
returns the current temperature for the city.

Example Output
Where are you? Chicago IL
Chicago weather:
65 degrees Fahrenheit
'''
import requests

#placeholder for your api key
api_key = "295d9d6c85a7f2922f813e39a2dd2a0a"
city_name = input("Type your city name (applicable only for US people: ")
URL = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": city_name,
    "appid": api_key,
    "units": "metrics"
}

response = requests.get(URL, params=params)
print(response.json())


#convert json text to python objects
data = response.json()

#print the temperature
print(f"The current temperature is: {data['main']['temp']}")
print(f"The min temperature of the day is: {data['main']['temp_min']}")
print(f"The max temperature of the day is: {data['main']['temp_max']}")


