from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS

RASA_URL = "http://localhost:5005/webhooks/rest/webhook"

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    print(f"Received message: {user_message}")
    
    response = requests.post(RASA_URL, json={"sender": "user", "message": user_message})
    
    # Log the response from Rasa
    print(f"Rasa response: {response.json()}")
    
    return jsonify(response.json())


if __name__ == "__main__":
    app.run(port=8000)
