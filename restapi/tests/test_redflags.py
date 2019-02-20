from .base import TestDb
import json


class TestRedflags(TestDb):

    def test_post_redflag(self):
        token = self.create_token()
        redflag_data = {
            "name": "Corruption at BOU",
            "description": "Misappropriation of funds",
            "location": "Kanjyokya street",
            "images": "home/fundmisuse.jpeg",
            "comment": "This is shocking"
        
        }
        res = self.app.post(
            '/api/v1/incidents/redflags', content_type='application/json',
            headers={'x-access-token': token}, data=json.dumps(redflag_data))
        self.assertEqual(res.status_code, 201)
        response = json.loads(res.data.decode())
        self.assertEqual(response['status'], 201)

    def test_post_redflag_without_token(self):
        token = self.create_token()
        redflag_data = {
            "name": "Corruption at BOU",
            "description": "Misappropriation of funds",
            "location": "Kanjyokya street",
            "images": "home/fundmisuse.jpeg",
            "comment": "This is shocking"
        }
        res = self.app.post(
            '/api/v1/incidents/redflags', content_type='application/json',
             data=json.dumps(redflag_data))
        self.assertEqual(res.status_code, 400)
        response = json.loads(res.data.decode())
        self.assertEqual(response['error'], "token is missing!")

    def test_get_one_redflag(self):
        token = self.create_token()
        redflag_data = {
            "name": "Corruption at BOU",
            "description": "Misappropriation of funds",
            "location": "Kanjyokya street",
            "images": "home/fundmisuse.jpeg",
            "comment": "This is shocking"
        }
        res = self.app.post(
            '/api/v1/incidents/redflags', content_type='application/json',
            headers={'x-access-token': token}, data=json.dumps(redflag_data))
        self.assertEqual(res.status_code, 201)
        response = self.app.get(
            '/api/v1/incidents/redflags/1', content_type='application/json',
            headers={'x-access-token': token})

        self.assertEqual(response.status_code, 200)

    def test_get_all_redflags(self):
        token = self.create_token()
        redflag_data = {
            "name": "Corruption at BOU",
            "description": "Misappropriation of funds",
            "location": "Kanjyokya street",
            "images": "home/fundmisuse.jpeg",
            "comment": "This is shocking"
        }
        res = self.app.post(
            '/api/v1/incidents/redflags', content_type='application/json',
            headers={'x-access-token': token}, data=json.dumps(redflag_data))
        self.assertEqual(res.status_code, 201)
        response = self.app.get(
            '/api/v1/incidents/redflags', content_type='application/json',
            headers={'x-access-token': token})

        self.assertEqual(response.status_code, 200)

    def test_delete_a_redflags(self):
        token = self.create_token()
        redflag_data = {
            "name": "Corruption at BOU",
            "description": "Misappropriation of funds",
            "location": "Kanjyokya street",
            "images": "home/fundmisuse.jpeg",
            "comment": "This is shocking"
        }
        res = self.app.post(
            '/api/v1/incidents/redflags', content_type='application/json',
            headers={'x-access-token': token}, data=json.dumps(redflag_data))
        self.assertEqual(res.status_code, 201)
        response = self.app.delete(
            '/api/v1/incidents/redflags/1', content_type='application/json',
            headers={'x-access-token': token})

        self.assertEqual(response.status_code, 200)

    def test_update_redflag_location(self):
        token = self.create_token()
        redflag_data = {
            "name": "Corruption at BOU",
            "description": "Misappropriation of funds",
            "location": "Kanjyokya street",
            "images": "home/fundmisuse.jpeg",
            "comment": "This is shocking"
        }
        res = self.app.post(
            '/api/v1/incidents/redflags', content_type='application/json',
            headers={'x-access-token': token}, data=json.dumps(redflag_data))
        self.assertEqual(res.status_code, 201)
        location_data = {
            "location": "Cafe Javas Kisementi"
        }
        resp = self.app.patch(
            '/api/v1/incidents/redflags/1/location', content_type='application/json',
            headers={'x-access-token': token}, data=json.dumps(location_data))
        self.assertEqual(resp.status_code, 201)

    def test_update_redflag_comment(self):
        token = self.create_token()
        redflag_data = {
            "name": "Corruption at BOU",
            "description": "Misappropriation of funds",
            "location": "Kanjyokya street",
            "images": "home/fundmisuse.jpeg",
            "comment": "This is shocking"
           
        }
        res = self.app.post(
            '/api/v1/incidents/redflags', content_type='application/json',
            headers={'x-access-token': token}, data=json.dumps(redflag_data))
        self.assertEqual(res.status_code, 201)
        comment_data = {
            "comment": "Misuse of funds in NGO project"
        }
        resp = self.app.patch(
            '/api/v1/incidents/redflags/1/comment', content_type='application/json',
            headers={'x-access-token': token}, data=json.dumps(comment_data))
        self.assertEqual(resp.status_code, 201)

    # def test_update_redflag_status(self):
    #     token = self.create_token()
    #     redflag_data = {
    #         "name": "Corruption at BOU",
    #         "description": "Misappropriation of funds",
    #         "location": "Kanjyokya street",
    #         "images": "home/fundmisuse.jpeg",
    #         "comment": "This is shocking"
    #     }
    #     res = self.app.post(
    #         '/api/v1/incidents/redflags', content_type='application/json',
    #         headers={'x-access-token': token}, data=json.dumps(redflag_data))
    #     self.assertEqual(res.status_code, 201)
    #     status_data = {
    #         "status": "resolved"
    #     }
    #     resp = self.app.patch(
    #         '/api/v1/incidents/redflags/1/status', content_type='application/json',
    #         headers={'x-access-token': token}, data=json.dumps(status_data))
    #     self.assertEqual(resp.status_code, 400)


    





    




   