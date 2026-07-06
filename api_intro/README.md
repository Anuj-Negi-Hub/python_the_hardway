# Basic REST API Servers and Clients Walkthrough

This directory contains basic REST API server implementations (FastAPI and Flask) and their corresponding client scripts to demonstrate standard HTTP request/response interactions.

---

## Project Structure

### 1. FastAPI Implementation
- **[server.py](file:///d:/Python/python_the_hard_way/python_the_hardway/api_intro/server.py)**: The FastAPI server hosting GET and POST endpoints (running on port `8000`).
- **[client.py](file:///d:/Python/python_the_hard_way/python_the_hardway/api_intro/client.py)**: The Python client script to query the FastAPI server.

### 2. Flask Implementation
- **[flask_server.py](file:///d:/Python/python_the_hard_way/python_the_hardway/api_intro/flask_server.py)**: The Flask server hosting identical GET and POST endpoints (running on port `5000`).
- **[flask_client.py](file:///d:/Python/python_the_hard_way/python_the_hardway/api_intro/flask_client.py)**: The Python client script to query the Flask server.

### 3. Flask Books API (Two-Endpoint Example)
- **[flask_books_server.py](file:///d:/Python/python_the_hard_way/python_the_hardway/api_intro/flask_books_server.py)**: A Flask server managing a list of books with GET and POST endpoints (running on port `5001`).
- **[flask_books_client.py](file:///d:/Python/python_the_hard_way/python_the_hardway/api_intro/flask_books_client.py)**: The Python client script to query the Flask Books API server.

---

## Installation & Setup

### Install Prerequisites

Make sure the required dependencies are installed:
```bash
pip install fastapi uvicorn flask requests
```

---

## How to Run

### Option A: FastAPI Server & Client

1. **Start the FastAPI Server**
   ```bash
   python api_intro/server.py
   ```
   *Note: Runs locally at `http://127.0.0.1:8000` with auto-reload.*

2. **Run the FastAPI Client**
   In a separate terminal, run:
   ```bash
   python api_intro/client.py
   ```

3. **FastAPI Interactive Docs**
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

### Option B: Flask Server & Client

1. **Start the Flask Server**
   ```bash
   python api_intro/flask_server.py
   ```
   *Note: Runs locally at `http://127.0.0.1:5000` with debug mode.*

2. **Run the Flask Client**
   In a separate terminal, run:
   ```bash
   python api_intro/flask_client.py
   ```

---

### Option C: Flask Books Server & Client (Two-Endpoint Example)

1. **Start the Flask Books Server**
   ```bash
   python api_intro/flask_books_server.py
   ```
   *Note: Runs locally at `http://127.0.0.1:5001` with debug mode.*

2. **Run the Flask Books Client**
   In a separate terminal, run:
   ```bash
   python api_intro/flask_books_client.py
   ```

---

## API Endpoints & Details (Basic)

Both `server.py` and `flask_server.py` implement the following three endpoints:

### 1. Home Endpoint (GET `/`)
- **Expected Response (FastAPI)**:
  ```json
  {
    "message": "Welcome to the basic FastAPI server!",
    "status": "running"
  }
  ```
- **Expected Response (Flask)**:
  ```json
  {
    "message": "Welcome to the basic Flask server!",
    "status": "running"
  }
  ```

### 2. Query Item Endpoint (GET `/items/{item_id}`)
- **Example Client Call**: `GET /items/42?q=search_term`
- **Expected Response**:
  ```json
  {
    "item_id": 42,
    "query_param": "search_term",
    "status": "success"
  }
  ```

### 3. Payload Submit Endpoint (POST `/submit`)
- **JSON Request Body**:
  ```json
  {
    "name": "Widget Deluxe",
    "description": "An advanced widget for testing payloads",
    "value": 100.0,
    "tax": 0.15
  }
  ```
- **Expected Response**:
  ```json
  {
    "received_payload": {
      "name": "Widget Deluxe",
      "description": "An advanced widget for testing payloads",
      "value": 100.0,
      "tax": 0.15
    },
    "calculated_total": 115.0,
    "message": "Hello Widget Deluxe, your payload was processed successfully."
  }
  ```
