import base64
import requests
import unittest

stt = "http://localhost:3003/stt"

class Testing(unittest.TestCase):

    ###########################################################
    ## Test [1] ##
    ###########################################################
    def test1(self):
        with open("answer.wav", "rb") as f:
            audio_data = f.read()

        encoded_audio = base64.b64encode(audio_data).decode("ascii")
        hdrs = {"Content-Type": "application/json"}
        js = {"speech": encoded_audio}

        rsp = requests.post(stt, headers=hdrs, json=js)

        if rsp.status_code == 200:
            recognized_text = rsp.json().get("text")
            print("Recognized Text:", recognized_text)

        self.assertEqual(rsp.status_code, 200)

if __name__ == "__main__":
    unittest.main()
