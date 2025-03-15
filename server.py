from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

DATA_FILE = 'captured_inputs.json'

# Initialize the JSON file if it doesn't exist
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump([], f)  # Start with an empty list

@app.route('/')
def index():
    return "NO data received"

@app.route('/handle_inputs', methods=['POST'])
def handle_inputs():
    """Receives and stores input data in a JSON file."""
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No JSON data provided"}), 400

        # Load existing data
        with open(DATA_FILE, 'r') as f:
            existing_data = json.load(f)

        # Append new data
        existing_data.append(data)

        # Save updated data
        with open(DATA_FILE, 'w') as f:
            json.dump(existing_data, f, indent=4)  # indent for readability

        print("Received and stored data:", data)
        return jsonify({"message": "Data received and stored successfully"}), 200

    except Exception as e:
        print(f"Error processing data: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    print("\nFor more information on how to use this tool, visit this tutorial link for free:")
    print("https://github.com/pulse-empire/veneer/tree/extension\n")
    app.run(debug=True, host='0.0.0.0', port=5000)