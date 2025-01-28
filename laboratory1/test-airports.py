import requests
import unittest
import database 

airports = "http://localhost:3000/airports"

class Testing(unittest.TestCase):
    ###########################################################
    ## Setup                                                 ##
    ###########################################################
    def setUp(self):
        self.airports_url = airports
        self.headers = {"Content-Type": "application/json"}
        database.db.clear()  # Ensure the database is clear before each test

    ###########################################################
    ## Test [1]                                              ##
    ###########################################################
    def test_insert_new_airport(self):
        code = "LAX"
        name = "Los Angeles"

        payload = {"code": code, "name": name}
        response = requests.put(f"{self.airports_url}/{code}", headers=self.headers, json=payload)

        self.assertEqual(response.status_code, 201)

    ###########################################################
    ## Test [2]                                              ##
    ###########################################################
    def test_update_existing_airport(self):
        code = "LAX"
        name = "Los Angeles"
        updated_name = "Los Angeles International"

        # Insert an airport
        requests.put(f"{self.airports_url}/{code}", headers=self.headers, json={"code": code, "name": name})

        # Update the airport
        response = requests.put(f"{self.airports_url}/{code}", headers=self.headers, json={"code": code, "name": updated_name})
        self.assertEqual(response.status_code, 204)

        # Verify the update
        airport = database.db.lookup(code)
        self.assertIsNotNone(airport)
        self.assertEqual(airport["name"], updated_name)

    ###########################################################
    ## Test [3]                                              ##
    ###########################################################
    def test_invalid_input(self):
        code = "LAX"
        invalid_payload = {"code": None, "name": "Los Angeles"}

        response = requests.put(f"{self.airports_url}/{code}", headers=self.headers, json=invalid_payload)
        self.assertEqual(response.status_code, 400)

    ###########################################################
    ## Test [4]                                              ##
    ###########################################################
    def test_clear_database(self):
        code = "LAX"
        name = "Los Angeles"

        # Insert an airport
        requests.put(f"{self.airports_url}/{code}", headers=self.headers, json={"code": code, "name": name})

        # Clear the database
        database.db.clear()

        # Verify the database is empty
        airport = database.db.lookup(code)
        self.assertIsNone(airport)

    ###########################################################
    ## Test [5]                                              ##
    ###########################################################
    def test_insert_duplicate_airport(self):
        code = "LAX"
        name = "Los Angeles"

        # Insert an airport
        requests.put(f"{self.airports_url}/{code}", headers=self.headers, json={"code": code, "name": name})

        # Attempt to insert the same airport again
        response = requests.put(f"{self.airports_url}/{code}", headers=self.headers, json={"code": code, "name": name})

        # Verify the response
        self.assertEqual(response.status_code, 204)  # Should update instead of duplicate

    ###########################################################
    ## Test [6]                                              ##
    ###########################################################
    def test_lookup_airport(self):
        code = "LAX"
        name = "Los Angeles"

        # Insert an airport
        requests.put(f"{self.airports_url}/{code}", headers=self.headers, json={"code": code, "name": name})

        # Retrieve the airport
        airport = database.db.lookup(code)

        # Verify the airport exists
        self.assertIsNotNone(airport)
        self.assertEqual(airport["code"], code)
        self.assertEqual(airport["name"], name)