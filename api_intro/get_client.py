import requests

URL = "http://127.0.0.1:8000"

response = requests.get(URL)

if response.status_code == 200:
    users = response.json()

    for user in users:
        print(f"ID    : {user['id']}")
        print(f"Name  : {user['name']}")
        print(f"Email : {user['email']}")
        print("-" * 30)

else:
    print("Request failed.")