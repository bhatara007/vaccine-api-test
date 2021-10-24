import json
import unittest
from jsonschema.validators import validate
import requests
import datetime
from datetime import timedelta
from jsonschema import validate

today = datetime.date.today()
URL = "https://suchonsite-server.herokuapp.com/getDataFromGov"

class ServiceSiteGetDataFromGovAPITest(unittest.TestCase):
    """
    Test ID: 11
    Test API to add the existed data to our database status code
    """
    def test_add_exist_data_to_data_status_code(self):
        api = URL + '20-10-2021'
        response = requests.post(api)
        #should return 401 status code
        self.assertEqual(response.status_code, 401)
    
    """
    Test ID: 12
    Test API for fetchinh data failed from goverment 
    """
    def test_fetch_data_failed_status_code(self):
        api = URL + '19-1-1999'
        response = requests.post(api)
        #should return 401 status code
        self.assertEqual(response.status_code, 504)
    