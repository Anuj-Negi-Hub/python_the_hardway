import requests

url = "https://mynotes-api-f3f0c-default-rtdb.asia-southeast1.firebasedatabase.app/notes.json"

#posting/uploading data to firebase
data = {
    "text": "Learn how to invert binary trees"
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())

#getting data from the firebase

url = "https://mynotes-api-f3f0c-default-rtdb.asia-southeast1.firebasedatabase.app/notes.json"
response = requests.get(url)

print(response.json())