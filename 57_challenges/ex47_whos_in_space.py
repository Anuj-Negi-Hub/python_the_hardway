'''
Create a program that pulls in this data and displays the information from this API in a tabular format.
URL: http://api.open-notify.org/astros.json

Example Output
There are 3 people in space right now:
Name | Craft
--------------------|------
Gennady Padalka | ISS
Mikhail Kornienko | ISS
Scott Kelly | ISS
'''
import requests
import json

URL = "http://api.open-notify.org/astros.json"

#get the data from URL
data = requests.get(URL)
#convert json data to python readable data 
data_json = data.json()

# print(data.json())

#count the total people in the space
print(f"There are {data_json['number']} people in space right now.")
print("Name                |  Craft")
print("--------------------|------")
count = 0

#prints the each person name with the space craft name
for person in data_json['people']:
    print(f"{person['name']:<20}|{person['craft']:>5}")
    count += 1