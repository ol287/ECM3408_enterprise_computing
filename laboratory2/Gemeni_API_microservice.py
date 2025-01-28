import os
import requests
from flask import Flask, request

# Load the API key from the environment variable
KEY2 = os.environ["KEY2"]

# API endpoint for the Gemini 1.5 language model
PATH = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=" + KEY2

# Initialize a Flask application
app = Flask(__name__)

# Define a route '/gemini' that accepts POST requests
@app.route('/gemini', methods=["POST"])
def endpoint():
    # Get the JSON payload from the incoming request
    js = request.get_json()

    # Extract the "question" field from the JSON payload
    question = js.get("question")

    # Check if a "question" is provided in the request
    if question is not None:
        # Set up the request headers for the API call
        hdrs = {"Content-Type": "application/json"}

        # Create the JSON payload for the Gemini API request
        js = {"contents": [{"parts": [{"text": question}]}]}

        # Send a POST request to the Gemini API with headers and payload
        rsp = requests.post(PATH, headers=hdrs, json=js)

        # Check if the API responded with a successful status code (200 OK)
        if rsp.status_code == 200:
            # Parse the response JSON to extract the generated answer
            answer = rsp.json()["candidates"][0]["content"]["parts"][0]["text"]

            # Return the answer in JSON format with a 200 status code
            return {"answer": answer}, 200  # OK
        else:
            # Return a 500 error if the API call failed
            return "", 500  # Internal Server Error
    else:
        # Return a 400 error if the "question" field is missing
        return "", 400  # Bad Request

# Entry point for the Flask application
if __name__ == "__main__":
    # Run the Flask app on localhost at port 3003
    app.run(host="localhost", port=3003)
