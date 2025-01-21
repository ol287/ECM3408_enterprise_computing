import requests
import unittest
import database 

airports = "http://localhost:3000/airports"

class Testing(unittest.TestCase):
  ###########################################################
  ## Test [1]                                              ##
  ###########################################################
  def test1(self):
    database.db.clear()
    code = "LAX"
    name = "Los Angeles"

    hdrs = {"Content-Type":"application/json"}
    js   = {"code":code,"name":name}
    rsp  = requests.put(f'{airports}/{code}',headers=hdrs,
             json=js)

    self.assertEqual(rsp.status_code,201)
