import unittest
from restapi import app
from restapi.models.database import DatabaseConnect
import json


class TestDb(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.db = DatabaseConnect()
        self.db.create_tables()

    def tearDown(self):
        self.db.drop_tables()

    def create_token(self):
        user_signup_data = {"first_name": "Jean",
                            "last_name": "kaboha",
                            "othernames": "mark",
                            "password": "yfhv7dtdsd7",
                            "email": "kjmdfffh@hoo.com",
                            "phone_number": "0758675645",
                            "username": "Thomas"}

        req = self.app.post(
            '/api/v1/auth/signup', content_type='application/json', data=json.dumps(user_signup_data))
        response = json.loads(req.data.decode())
        user_signin_data = {
            "username": "Thomas",
            "password": "yfhv7dtdsd7"
        }
        req = self.app.post(
            '/api/v1/auth/login', content_type='application/json', data=json.dumps(user_signin_data))
        signin_response = json.loads(req.data.decode())
        data_list = signin_response['token']
        return data_list

if __name__ == '__main__':
    unittest.main()
