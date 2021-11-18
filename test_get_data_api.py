import json
import unittest
from jsonschema.validators import validate
import requests
import datetime
from datetime import timedelta
from jsonschema import validate

today = datetime.date.today()
URL = "https://suchonsite-server.herokuapp.com/people"

class ServiceSiteGetDataByDateAPITest(unittest.TestCase):

    def test_get_people_by_date_status_code(self):
        """
        Test ID: 1
        Test API endpoint by correct date format with status code
        """
        current_day = '20-10-2021' #we only have a data for 20-10-2021
        api = URL + "/by_date/" + current_day
        res = requests.get(api)
        self.assertEqual(200, res.status_code)
    
    def test_get_people_by_date(self):
        """
        Test ID: 2
        Test API endpoint with current day and correct date format we should get the data with the same date that
        we requested
        """
        current_day = '20-10-2021' #we only have a data for 20-10-2021
        api = URL + "/by_date/" + current_day
        res = requests.get(api)
        people = res.json()
        self.assertEqual(people['date'], current_day)

    def test_get_people_by_wrong_date_format_1(self):
        """
        Test ID: 3
        Test API endpoint with wrong date format
        """
        wrong_current_day = today.strftime('%d/%m/%Y')
        api = URL + "/by_date/" + wrong_current_day
        res = requests.get(api)
        self.assertEqual(404, res.status_code)
    
    def test_get_people_schema_structure(self):
        """
        Test ID: 4
        Test API response JSON schema structure
        """
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

    def test_get_people_by_future_date(self):
        """
        Test ID: 5
        Test API endpoint status code with future day data 
        """
        future_date = (today + timedelta(5)).strftime('%d-%m-%Y')
        api = URL + "/by_date/" + future_date
        res = requests.get(api)
        self.assertEqual(202, res.status_code)
    
    def test_get_person_schema_structure(self):
        """
        Test ID: 6
        Test API response person JSON schema structure
        """
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
                "priority" : {"type" : "string"},
                "vac_time" : {"type" : "string"}
            },
        }
        test_day = "20-10-2021"
        api = URL + "/by_date/" + test_day
        response = requests.get(api).json()
        for person in response['people']:
            #if both JSON format are the same validate() method will return None Otherwise 
            #it will throws error exception
            self.assertIsNone(validate(instance=person, schema=schema))
    
    def test_check_type_of_response_2(self):
        """
        Test ID: 7
        Test for check whether response data is JSON or not?
        """
        api = URL + "/by_date/20-10-2021"
        response = requests.get(api)
        self.assertEqual(response.headers.get('content-type'), 'application/json; charset=utf-8')
    
    def test_get_people_by_wrong_date_format_2(self):
        """
        Test ID: 8
        Test API endpoint with wrong date format
        """
        wrong_current_day = "10-OCT-2021"
        api = URL + "/by_date/" + wrong_current_day
        res = requests.get(api)
        self.assertEqual(404, res.status_code)
    
    def test_get_all_data_status_code(self):
        """
        Test ID: 9
        Test API get all data status code
        """
        api = URL + "/all/"
        response = requests.get(api)
        self.assertEqual(response.status_code, 200)
    
    def test_check_type_of_response_1(self):
        """
        Test ID: 10
        Test for check whether response data is JSON or not?
        """
        api = URL + "/all/"
        response = requests.get(api)
        self.assertEqual(response.headers.get('content-type'), 'application/json; charset=utf-8')
    
    def test_add_exist_data_to_data_status_code(self):
        """
        Test ID: 11
        Test API to add the existed data to our database status code
        """
        api = URL + '20-10-2021'
        response = requests.post(api)
        #should return 401 status code
        self.assertEqual(response.status_code, 401)
    
    def test_fetch_data_failed_status_code(self):
        """
        Test ID: 12
        Test API for fetchinh data failed from goverment 
        """
        api = URL + '19-1-1999'
        response = requests.post(api)
        #should return 504 failed status code
        self.assertEqual(response.status_code, 504)

            

        
if __name__ == '__main__':
    unittest.main()