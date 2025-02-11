import requests
import base64
import json

def test_alexa_microservice():
    # Load a sample audio file and encode it as base64
    with open("answer.wav", "rb") as audio_file:
        encoded_audio = base64.b64encode(audio_file.read()).decode("utf-8")
    
    # Construct the request payload
    payload = {"speech": encoded_audio}
    
    # Send a POST request to the Alexa microservice
    url = "http://localhost:3004/alexa"
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, headers=headers, json=payload)
    
    # Check response status
    if response.status_code == 200:
        print("Test Passed: Received 200 OK")
        response_data = response.json()
        if "speech" in response_data:
            print("Response contains speech data.")
        else:
            print("Test Failed: Response does not contain expected speech data.")
    else:
        print(f"Test Failed: Received status code {response.status_code}")
        print("Response body:", response.text)

if __name__ == "__main__":
    test_alexa_microservice()
