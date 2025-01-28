import requests
import unittest

alpha = "http://localhost:3003/alpha"

class Testing(unittest.TestCase):
  ###########################################################
  ## Test [1]                                              ##
  ###########################################################
  def test1(self):
    question = "What is the melting point of silver?"
    answer   = "961"

    hdrs = {"Content-Type":"application/json"}
    js   = {"question":question}
    rsp  = requests.post(alpha,headers=hdrs,json=js)

    self.assertEqual(rsp.status_code,200)
    self.assertTrue(answer in rsp.json()["answer"])
