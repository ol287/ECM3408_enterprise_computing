import base64
import os
import requests
from flask import Flask, request

KEY = os.environ["KEY"]
REG = "uksouth"
URI = "https://" + REG + ".stt.speech.microsoft.com/speech/recognition/conversation/cognitiveservices/v1"

app = Flask(__name__)

@app.route("/stt", methods=["POST"])
def endpoint():
    js = request.get_json()
    s = js.get("speech")

    if s is not None:
        try:
            audio_data = base64.b64decode(s)
            text = work(audio_data)
            if text is not None:
                return {"text": text}, 200  # OK
            else:
                return "", 500  # Internal Server Error
        except Exception as e:
            return str(e), 500  # Internal Server Error
    else:
        return "", 400  # Bad Request

def work(audio_data):
    hdrs = {
        "Content-Type": "audio/wav",
        "Ocp-Apim-Subscription-Key": KEY,
    }
    params = {
        "language": "en-US",
        "format": "simple"
    }
    rsp = requests.post(URI, headers=hdrs, params=params, data=audio_data)

    if rsp.status_code == 200:
        return rsp.json().get("DisplayText")
    else:
        return None

if __name__ == "__main__":
    app.run(host="localhost", port=3003)