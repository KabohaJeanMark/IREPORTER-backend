from .base import TestDb
import json

class TestEndpoints(TestDb):

    def test_index(self):
        response = self.app.get('/api/v1/')
        self.assertEqual(response.status_code, 200)
        data = response.data.decode()
        message = {
            "Message": "Welcome to Ireporter"}
        self.assertEqual(json.loads(data), message)

    def test_signup(self):

        data = {
            "first_name": "Jean",
            "last_name": "kaboha",
            "othernames": "mark",
            "password": "yfhv7dtdsd7",
            "email": "kjmdfffh@hoo.com",
            "phone_number": "0758675645",
            "username": "Thomas"
        }
        res = self.app.post(
            '/api/v1/auth/signup', content_type='application/json', data=json.dumps(data))
        response = json.loads(res.data.decode())
        d = response['data']
        self.assertEqual(d[0]['message'], "User has been succesfully created")
        self.assertEqual(res.status_code, 201)

    def test_valid_sign_in(self):
        data = {
            "first_name": "Jean",
            "last_name": "kaboha",
            "othernames": "mark",
            "password": "yfhv7dtdsd7",
            "email": "kjmdfffh@hoo.com",
            "phone_number": "0758675645",
            "username": "Thomas"
        }
        resp = self.app.post(
            '/api/v1/auth/signup', content_type='application/json', data=json.dumps(data))
        login_data = {
            "username": "Thomas",
            "password": "yfhv7dtdsd7"
        }
        res = self.app.post(
            '/api/v1/auth/login', content_type='application/json', data=json.dumps(login_data))
        self.assertEqual(res.status_code, 200)

    def test_invalid_signin(self):
        data = {
            "first_name": "Jean",
            "last_name": "kaboha",
            "othernames": "mark",
            "password": "yfhv7dtdsd7",
            "email": "kjmdfffh@hoo.com",
            "phone_number": "0758675645",
            "username": "Thomas"
        }
        resp = self.app.post(
            '/api/v1/auth/signup', content_type='application/json', data=json.dumps(data))
        invalid_signin = {
            "username": "Jerry",
            "password": "montblanc2433"
        }
        res = self.app.post(
            '/api/v1/auth/login', content_type='application/json', data=json.dumps(invalid_signin))
        self.assertEqual(res.status_code, 400)

    def test_signup_with_same_username(self):
        data = {
            "first_name": "Jack",
            "last_name": "Donovan",
            "othernames": "Mugembe",
            "password": "yfhv7dtdsd7",
            "email": "jdm@yahoo.com",
            "phone_number": "0758675645",
            "username": "jackdonovan"
        }
        res = self.app.post(
            '/api/v1/auth/signup', content_type='application/json', data=json.dumps(data))
        repeat_username = {
            "first_name": "Jack",
            "last_name": "Donovan",
            "othernames": "Mugembe",
            "password": "yfhv7dry",
            "email": "tom@yahoo.com",
            "phone_number": "0789653423",
            "username": "jackdonovan"
        }
        res = self.app.post(
            '/api/v1/auth/signup', content_type='application/json', data=json.dumps(repeat_username))
        self.assertEqual(res.status_code, 400)
        resp = json.loads(res.data.decode())
        self.assertEqual(resp['message'], "That username already exists")
        self.assertEqual(resp['status'], 400)
