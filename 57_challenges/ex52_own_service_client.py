import requests

url = "http://127.0.0.1:8000/time"

data = requests.get(url)
print(data.json())