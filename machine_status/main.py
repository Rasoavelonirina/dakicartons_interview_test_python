from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# In-memory machine data information
machine_data = {
    "id": 1,
    "name": "DELL G450",
    "description": "Machine for processing "
}

# Allowed statuses
ALLOWED_STATUSES = {"STARTED", "COMPLETED", "IDLE", "ERROR"}

@app.route('/data', methods=['GET'])
def get_data():
    # Process and return some machine data
    # As an example, Rondomly set some exploitable data information

    machine_data['status'] = random.choice(list(ALLOWED_STATUSES))
    machine_data['temperature'] = round(random.uniform(20.0, 100.0), 2)    # °C
    machine_data["fan_speed"] = round(random.uniform(0.0, 1000.0), 2)      # tr/mn
    return jsonify(machine_data), 200


@app.route('/status', methods=['POST'])
def update_status():
    data = request.json
    if not data or 'status' not in data:
        return jsonify({"error": "Missing 'status' field in request data"}), 400

    new_status = data.get('status').upper()
    # Validate input
    if new_status not in ALLOWED_STATUSES:
        return jsonify({"error": f"Invalid status. Allowed statuses: {', '.join(ALLOWED_STATUSES)}"}), 400

    # Update the status
    machine_data["status"] = new_status
    return jsonify({"message": "Status updated"}), 200


if __name__ == '__main__':
    app.run(debug=True)
