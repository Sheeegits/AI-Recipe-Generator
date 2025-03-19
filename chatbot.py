import streamlit as st
import requests

# Set Flask API server URL
FLASK_API_URL = "http://localhost:8000/chat"

def send_message_to_flask(message):
    try:
        # Send POST request to Flask API
        response = requests.post(FLASK_API_URL, json={"message": message})
        
        # Check if the response status is OK
        if response.status_code == 200:
            return response.json()
        else:
            st.write(f"Error: Received {response.status_code} from Flask API")
            return None
    except requests.exceptions.RequestException as e:
        st.write(f"An error occurred: {e}")
        return None

# Streamlit app to get input from user
st.title("AI Recipe Generator")

# Get the user input
user_message = st.text_input("Ask for a recipe:")

# Check if the user has entered a message
if user_message:
    st.write(f"User: {user_message}")  # Show user's input
    response = send_message_to_flask(user_message)
    
    # Check if the response was received
    if response:
        if isinstance(response, list):
            for message in response:
                st.write(message.get("text"))
        else:
            st.write("No response from Rasa.")
    else:
        st.write("No response from Flask API.")
