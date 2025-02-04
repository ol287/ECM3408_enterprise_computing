import base64
import requests
import unittest

tts = "http://localhost:3002/tts"

class Testing(unittest.TestCase):
  ###########################################################
  ## Test [1]                                              ##
  ###########################################################
  def test1(self):
    text = "What is the melting point of silver?"

    hdrs = {"Content-Type":"application/json"}
    js   = {"text":text}
    rsp  = requests.post(tts,headers=hdrs,json=js)

    speech = rsp.json()["speech"]
    wav    = base64.b64decode(speech)
    f      = open("answer.wav","wb")
    f.write(wav)
    f.close()

    self.assertEqual(rsp.status_code,200)
    # verify speech somehow?
