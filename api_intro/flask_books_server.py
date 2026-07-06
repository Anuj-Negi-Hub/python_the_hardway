from flask import Flask, request, jsonify

app = Flask(__name__)

# Simple in-memory books database
books = [
    {"id": 1, "title": "Python: The Hard Way", "author": "Zed Shaw"},
    {"id": 2, "title": "Fluent Python", "author": "Luciano Ramalho"}
]

# Endpoint 1: GET /books - Retrieve all books
@app.route("/books", methods=["GET"])
def get_books():
    return jsonify(books)

# Endpoint 2: POST /books - Add a new book
@app.route("/books", methods=["POST"])
def add_book():
    data = request.get_json(silent=True) or {}
    title = data.get("title")
    author = data.get("author")
    
    if not title or not author:
        return jsonify({"error": "Missing 'title' or 'author'"}), 400
        
    new_book = {
        "id": len(books) + 1,
        "title": title,
        "author": author
    }
    books.append(new_book)
    return jsonify(new_book), 201

if __name__ == "__main__":
    # Run server on port 5001 to avoid port conflicts with port 5000/8000
    app.run(host="127.0.0.1", port=5001, debug=True)
