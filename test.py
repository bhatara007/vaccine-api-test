import json
import unittest
from jsonschema.validators import validate
import requests
import datetime
from datetime import timedelta
from jsonschema import validate

today = datetime.date.today()
URL = "https://suchonsite-server.herokuapp.com/people"

class ServiceSiteAPITest(unittest.TestCase):

    """
    Test ID: 1
    Test API endpoint by correct date format with status code
    """
    def test_get_people_by_date_status_code(self):
        current_day = today.strftime('%d-%m-%Y')
        api = URL + "/by_date/" + current_day
        res = requests.get(api)
        self.assertEqual(200, res.status_code)
    
    """
    Test ID: 2
    Test API endpoint with current day and correct date format we should get the data with the same date that
    we requested
    """
    def test_get_people_by_date(self):
        current_day = '20-10-2021'
        api = URL + "/by_date/" + current_day
        res = requests.get(api)
        people = res.json()
        self.assertEqual(people['date'], current_day)

    """
    Test ID: 3
    Test API endpoint with wrong date format
    """
    def test_get_people_by_wrong_date_format(self):
        wrong_current_day = today.strftime('%d/%m/%Y')
        api = URL + "/by_date/" + wrong_current_day
        res = requests.get(api)
        self.assertEqual(404, res.status_code)
    
    """
    Test ID: 4
    Test API response JSON schema structure
    """
    def test_get_people_schema_structure(self):
        schema = {
            "type" : "object",
            "properties" : {
                "_id" : {"type" : "string"},
                "date" : {"type" : "string"},
                "people" : {"type" : "array"},
            },
        }
        test_day = "20-10-2021"
        api = URL + "/by_date/" + test_day
        response = requests.get(api).json()
        #if both JSON format are the same validate() method will return None Otherwise 
        #it will throws error exception
        self.assertIsNone(validate(instance=response, schema=schema))

    """
    Test ID: 5
    Test API endpoint status code with future day data 
    """
    def test_get_people_by_future_date(self):
        future_date = (today + timedelta(5)).strftime('%d-%m-%Y')
        api = URL + "/by_date/" + future_date
        res = requests.get(api)
        self.assertEqual(202, res.status_code)
    
    """
    Test ID: 6
    Test API response person JSON schema structure
    """
    def test_get_person_schema_structure(self):
        schema = {
            "type" : "object",
            "properties" : {
                "reservation_id" : {"type" : "number"},
                "register_timestamp" : {"type" : "string"},
                "name" : {"type" : "string"},
                "surname" : {"type" : "string"},
                "birth_date" : {"type" : "string"},
                "citizen_id" : {"type" : "string"},
                "occupation" : {"type" : "string"},
                "address" : {"type" : "string"},
            },
        }
        test_day = "20-10-2021"
        api = URL + "/by_date/" + test_day
        response = requests.get(api).json()
        for person in response['people']:
            self.assertIsNone(validate(instance=person, schema=schema))
    
    """
    Test ID: 7
    Test API get all data status code
    """
    def test_get_all_data_status_code(self):
        api = URL + "/all/"
        response = requests.get(api)
        self.assertEqual(response.status_code, 200)

            

        
if __name__ == '__main__':
    unittest.main()