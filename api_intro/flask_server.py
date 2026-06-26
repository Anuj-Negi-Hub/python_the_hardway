from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def read_root():
    return jsonify({
        "message": "Welcome to the basic Flask server!",
        "status": "running"
    })

@app.route("/items/<int:item_id>", methods=["GET"])
def read_item(item_id):
    q = request.args.get("q")
    return jsonify({
        "item_id": item_id,
        "query_param": q,
        "status": "success"
    })

@app.route("/submit", methods=["POST"])
def create_item():
    payload = request.get_json(silent=True) or {}
    
    # Simple validation
    name = payload.get("name")
    value = payload.get("value")
    
    if name is None or value is None:
        return jsonify({"error": "Missing required fields: 'name' and 'value'"}), 400
        
    description = payload.get("description")
    tax = payload.get("tax")
    
    try:
        value = float(value)
    except (ValueError, TypeError):
        return jsonify({"error": "'value' must be a number"}), 400
        
    total_value = value
    if tax is not None:
        try:
            tax = float(tax)
            total_value += value * tax
        except (ValueError, TypeError):
            return jsonify({"error": "'tax' must be a number"}), 400

    return jsonify({
        "received_payload": {
            "name": name,
            "description": description,
            "value": value,
            "tax": tax
        },
        "calculated_total": total_value,
        "message": f"Hello {name}, your payload was processed successfully."
    })

if __name__ == "__main__":
    # Run server locally on port 5000 (Flask's default port)
    app.run(host="127.0.0.1", port=5000, debug=True)
