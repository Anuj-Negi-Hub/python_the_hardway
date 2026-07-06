import requests

response = requests.get("http://127.0.0.1:8000/user")

print(response.json())
data = response.json()
print(f"id: {data['id']}")
print(f"name: {data['name']}")
print(f"city: {data['city']}")

res1 = requests.get("http://127.0.0.1:8000/get_length/himachal")
print(res1.json())