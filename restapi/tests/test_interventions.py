from .base import TestDb
import json


class TestIntervention(TestDb):

    def test_post_intervention(self):
        token = self.create_token()
        intervention_data = {
            "comment": "Power outage in Mulago",
            "images": "elec.jpeg",
            "location": "Mulago",
            "videos": "blackout.mp4"
        }
        res = self.app.post(
            '/api/v1/interventions', content_type='application/json',
            headers={'Authorization': f'Bearer {token}'}, data=json.dumps(intervention_data))
        self.assertEqual(res.status_code, 201)
        response = json.loads(res.data.decode())
        self.assertEqual(response['status'], 201)

    def test_post_intervention_without_token(self):
        token = self.create_token()
        intervention_data = {
            "comment": "Power outage in Mulago",
            "images": "elec.jpeg",
            "location": "Mulago",
            "videos": "blackout.mp4"
        }
        res = self.app.post(
            '/api/v1/interventions', content_type='application/json', data=json.dumps(intervention_data))
        self.assertEqual(res.status_code, 401)
        response = json.loads(res.data.decode())
        self.assertEqual(response['msg'], "Missing Authorization Header")

    def test_get_one_intervention(self):
        token = self.create_token()
        intervention_data = {
            "comment": "Power outage in Mulago",
            "images": "elec.jpeg",
            "location": "Mulago",
            "videos": "blackout.mp4"
        }
        res = self.app.post(
            '/api/v1/interventions', content_type='application/json',
            headers={'Authorization': f'Bearer {token}'}, data=json.dumps(intervention_data))
        self.assertEqual(res.status_code, 201)
        response = self.app.get(
            '/api/v1/interventions/1', content_type='application/json',
            headers={'Authorization': f'Bearer {token}'})

        self.assertEqual(response.status_code, 200)

    def test_get_all_interventions(self):
        token = self.create_token()
        intervention_data = {
            "comment": "Power outage in Mulago",
            "images": "elec.jpeg",
            "location": "Mulago",
            "videos": "blackout.mp4"
        }
        res = self.app.post(
            '/api/v1/interventions', content_type='application/json',
            headers={'Authorization': f'Bearer {token}'}, data=json.dumps(intervention_data))
        self.assertEqual(res.status_code, 201)
        response = self.app.get(
            '/api/v1/interventions', content_type='application/json',
            headers={'Authorization': f'Bearer {token}'}, data=json.dumps(intervention_data))
        self.assertEqual(response.status_code, 200)

    def test_get_a_single_user_intervention(self):
        token = self.create_token()
        intervention_data = {
        "comment": "Power outage in Mulago",
        "images": "elec.jpeg",
        "location": "Mulago",
        "videos": "blackout.mp4"
    }
    res = self.app.post(
        '/api/v1/interventions', content_type='application/json',
        headers={'Authorization': f'Bearer {token}'}, data=json.dumps(intervention_data))
    self.assertEqual(res.status_code, 201)
    response = self.app.get(
        '/api/v1/user/interventions/1', content_type='application/json',
        headers={'Authorization': f'Bearer {token}'}, data=json.dumps(intervention_data))
    self.assertEqual(response.status_code, 200)
