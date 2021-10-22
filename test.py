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

    def test_get_people_by_date_status_code(self):
        test_day = "20-10-2021"
        api = URL + "/by_date/" + test_day
        res = requests.get(api)
        self.assertEqual(200, res.status_code)

    def test_get_people_by_wrong_date_status_code(self):
        future_day = today + timedelta(days=5)
        api = URL + "/by_date/" + future_day.strftime('%d-%m-%Y')
        res = requests.get(api)
        self.assertEqual(404, res.status_code)
    
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