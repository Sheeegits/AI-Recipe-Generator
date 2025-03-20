from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

RASA_URL = "http://localhost:5005/webhooks/rest/webhook"

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    if not user_message:
        return jsonify({"error": "Message cannot be empty"}), 400  # Handle empty messages
    
    print(f"Received message: {user_message}")

    try:
        response = requests.post(
            RASA_URL,
            json={"sender": "user", "message": user_message},
            headers={"Content-Type": "application/json"}
        )

        # Log the response from Rasa
        rasa_response = response.json()
        print(f"Rasa response: {rasa_response}")

        return jsonify(rasa_response)

    except requests.exceptions.RequestException as e:
        print(f"Error connecting to Rasa: {e}")
        return jsonify({"error": "Could not connect to Rasa server"}), 500  # Handle connection errors

if __name__ == "__main__":
    app.run(port=8000, debug=False)
