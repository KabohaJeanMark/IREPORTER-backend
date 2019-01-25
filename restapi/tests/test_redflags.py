from .base import TestDb
import json


class TestRedflags(TestDb):

    def test_post_redflag(self):
        token = self.create_token()
        redflag_data = {
            "comment": "Misappropiate allocation of funds",
            "images": "bribe1.jpeg",
            "location": "Mbarara ",
            "videos": "bribe2.mp4"
        }
        res = self.app.post(
            '/api/v1/redflags', content_type='application/json',
            headers={'Authorization': f'Bearer {token}'}, data=json.dumps(redflag_data))
        self.assertEqual(res.status_code, 201)
        response = json.loads(res.data.decode())
        self.assertEqual(response['status'], 201)

    def test_post_redflag_without_token(self):
        token = self.create_token()
        redflag_data = {
            "comment": "Misappropiate allocation of funds",
            "images": "bribe1.jpeg",
            "location": "Mbarara ",
            "videos": "bribe2.mp4"
        }
        res = self.app.post(
            '/api/v1/redflags', content_type='application/json',
             data=json.dumps(redflag_data))
        self.assertEqual(res.status_code, 401)
        response = json.loads(res.data.decode())
        self.assertEqual(response['msg'], "Missing Authorization Header")

    def test_get_one_redflag(self):
        token = self.create_token()
        redflag_data = {
            "comment": "Misappropiate allocation of funds",
            "images": "bribe1.jpeg",
            "location": "Mbarara ",
            "videos": "bribe2.mp4"
        }
        res = self.app.post(
            '/api/v1/redflags', content_type='application/json',
            headers={'Authorization': f'Bearer {token}'}, data=json.dumps(redflag_data))
        self.assertEqual(res.status_code, 201)
        response = self.app.get(
            '/api/v1/redflags/1', content_type='application/json',
            headers={'Authorization': f'Bearer {token}'})

        self.assertEqual(response.status_code, 200)

    def test_get_all_redflags(self):
        token = self.create_token()
        redflag_data = {
            "comment": "Misappropiate allocation of funds",
            "images": "bribe1.jpeg",
            "location": "Mbarara ",
            "videos": "bribe2.mp4"
        }
        res = self.app.post(
            '/api/v1/redflags', content_type='application/json',
            headers={'Authorization': f'Bearer {token}'}, data=json.dumps(redflag_data))
        self.assertEqual(res.status_code, 201)
        response = self.app.get(
            '/api/v1/redflags', content_type='application/json',
            headers={'Authorization': f'Bearer {token}'})

        self.assertEqual(response.status_code, 200)

    




   