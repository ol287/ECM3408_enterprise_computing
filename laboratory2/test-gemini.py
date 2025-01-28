import requests
import unittest

gemini = "http://localhost:3003/gemini"

class Testing(unittest.TestCase):
    ###########################################################
    ## Test [1]                                              ##
    ###########################################################
    def test_valid_request(self):
        question = "What is the capital of France?"
        expected_answer = "Paris"

        # Define headers and payload
        hdrs = {"Content-Type": "application/json"}
        js = {"question": question}

        # Make a POST request to the /gemini endpoint
        rsp = requests.post(gemini, headers=hdrs, json=js)

        # Assertions
        self.assertEqual(rsp.status_code, 200)
        self.assertTrue(expected_answer in rsp.json()["answer"])

    ###########################################################
    ## Test [2]                                              ##
    ###########################################################
    def test_missing_question(self):
        # Payload with no 'question' field
        js = {}

        # Define headers
        hdrs = {"Content-Type": "application/json"}

        # Make a POST request to the /gemini endpoint
        rsp = requests.post(gemini, headers=hdrs, json=js)

        # Assertions
        self.assertEqual(rsp.status_code, 400)

    ###########################################################
    ## Test [3]                                              ##
    ###########################################################
    def test_api_failure(self):
        question = "This is a test causing API failure"

        # Define headers and payload
        hdrs = {"Content-Type": "application/json"}
        js = {"question": question}

        # Simulating API failure (assuming the backend handles it)
        rsp = requests.post(gemini, headers=hdrs, json=js)

        # Assertions
        self.assertTrue(rsp.status_code in [500, 502, 503])

if __name__ == "__main__":
    unittest.main()
