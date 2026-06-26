import requests
import json

BASE_URL = "http://127.0.0.1:8000"

def test_root():
    print("Testing GET / ...")
    try:
        response = requests.get(BASE_URL)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the server. Is it running?")
    print("-" * 50)

def test_get_item(item_id: int, query: str):
    print(f"Testing GET /items/{item_id} with query '{query}' ...")
    try:
        response = requests.get(f"{BASE_URL}/items/{item_id}", params={"q": query})
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the server. Is it running?")
    print("-" * 50)

def test_post_payload():
    print("Testing POST /submit with JSON payload ...")
    payload = {
        "name": "Widget Deluxe",
        "description": "An advanced widget for testing payloads",
        "value": 100.0,
        "tax": 0.15
    }
    try:
        headers = {"Content-Type": "application/json"}
        response = requests.post(f"{BASE_URL}/submit", data=json.dumps(payload), headers=headers)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the server. Is it running?")
    print("-" * 50)

if __name__ == "__main__":
    print("Starting client requests to FastAPI server...")
    print("=" * 50)
    test_root()
    test_get_item(42, "search_term")
    test_post_payload()
