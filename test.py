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
    Test API endpoint with current day and correct date format The response shouldn't be an empty JSON
    """
    def test_get_people_by_date(self):
        current_day = today.strftime('%d-%m-%Y')
        api = URL + "/by_date/" + current_day
        res = requests.get(api)
        people = res.json()
        self.assertNotEqual({}, people)

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
        
if __name__ == '__main__':
    unittest.main()