import requests
import json

URL = "http://127.0.0.1:5001/books"

def fetch_books():
    print("Fetching books...")
    try:
        response = requests.get(URL)
        if response.status_code == 200:
            print("Current library list:")
            for book in response.json():
                print(f"ID: {book['id']} |   Title: {book['title']} | Author: {book['author']}")
        else:
            print(f"Failed to fetch books. Status code: {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the books server. Is it running?")
    print("-" * 50)

def add_new_book(title, author):
    print(f"Adding new book: '{title}' by {author}...")
    payload = {"title": title, "author": author}
    try:
        response = requests.post(URL, json=payload)
        if response.status_code == 201:
            print("Successfully added:")
            print(json.dumps(response.json(), indent=2))
        else:
            print(f"Failed to add book. Status code: {response.status_code}")
            print(response.text)
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the books server. Is it running?")
    print("-" * 50)

if __name__ == "__main__":
    fetch_books()
    add_new_book("Learning Python", "Mark Lutz")
    fetch_books()
