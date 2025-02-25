import requests
import unittest
from factorial import app

mock = app.test_client()

class Testing(unittest.TestCase):
  ###########################################################
  ## Test [1]                                              ##
  ###########################################################
  def test1(self):
    trials = {
      "test1a" : (0,1),
      "test1b" : (1,1),
      "test1c" : (4,24),
      "test1d" : (6,720),
      "test1e" : (9,362880)
    }

    for name, (argument,result) in trials.items():
      with self.subTest(name=name):
        hdrs = {"Content-Type":"application/json"}
        js   = {"argument":argument}
        rsp  = mock.post("/factorial",headers=hdrs,json=js)

        self.assertEqual(rsp.status_code,200)
        self.assertEqual(result,rsp.json["result"])
