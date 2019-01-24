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

        data ={
                "first_name":"Jean",
                "last_name": "kaboha",
                "othernames": "mark",
                "password": "yfhv7dtdsd7",
                "email":"kjmdfffh@hoo.com",
                "phone_number":"0758675645",
                "username": "Thomas"
}
        res = self.app.post(
            '/api/v1/auth/signup', content_type='application/json', data=json.dumps(data))
        
        self.assertEqual(res.status_code,201)

    def test_valid_sign_in(self):
        data ={
                "first_name":"Jean",
                "last_name": "kaboha",
                "othernames": "mark",
                "password": "yfhv7dtdsd7",
                "email":"kjmdfffh@hoo.com",
                "phone_number":"0758675645",
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
        self.assertEqual(res.status_code,200)   

    def test_invalid_signin(self):
        data ={
                "first_name":"Jean",
                "last_name": "kaboha",
                "othernames": "mark",
                "password": "yfhv7dtdsd7",
                "email":"kjmdfffh@hoo.com",
                "phone_number":"0758675645",
                "username": "Thomas"
        }
        resp = self.app.post(
            '/api/v1/auth/signup', content_type='application/json', data=json.dumps(data))
        invalid_signin ={
            	"username": "Jerry",
	            "password": "montblanc2433"
        }   
        res = self.app.post(
            '/api/v1/auth/login', content_type='application/json', data=json.dumps(invalid_signin))
        self.assertEqual(res.status_code,400) 