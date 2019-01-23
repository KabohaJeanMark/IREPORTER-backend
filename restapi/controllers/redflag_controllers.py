from flask import request, jsonify
from datetime import datetime
from restapi.models.redflag_models import Interventions


class InterventionsController():

    def __init__(self):
        pass

    def create_intervention(self):

        interventions = Interventions()
        data = request.get_json()
        status = "draft"
        images = data.get("images")
        videos = data.get("videos")
        comment = data.get("comment")
        location = data.get("location")
        created_by = request.headers['user_id']

        postman_strings = [status, images, videos, comment, location]
        postman_data = [status, images, videos, comment, location]

        for value in postman_strings:
            if not isinstance(value, str):
                return jsonify({
                    "status": "404",
                    "message": "'{}' should be a string".format(value)
                })
        for v in postman_data:
            if not v:
                return jsonify({
                    "status": "400",
                    "message": "{} field is missing".format(v)
                })

        interv_id = interventions.add_intervention(location=data['location'],
                                                   status=data['status'],
                                                   images=data['images'],
                                                   videos=data['videos'],
                                                   comment=data['comment'],
                                                   created_by=request.headers['user_id']
                                                   )

        return jsonify({
            "status": 201,
            "data": [{
                "id": interv_id['intervention_id'],
                "message": "Created intervention record"
            }]
        })

    def get_all_interventions(self):
        intervention = Interventions().get_all_intervention_records()
        if intervention:
            return jsonify({'status': 200,
                            'data': intervention})
        return jsonify({'error': 'intervention not found'}), 400

    def get_all_a_users_interventions(self, user_id):
        single_user_interv = Interventions().get_all_interventions_by_specific_user(user_id)
        if single_user_interv:
            return jsonify({'status': 200,
                            'data': single_user_interv})
        return jsonify({'error': 'Intervention not found'}), 400

    def get_a_single_intervention(self, intervention_id):
        one_intervention = Interventions().get_one_intervention(intervention_id)
        if one_intervention:
            return jsonify({'status': 200,
                            'data': one_intervention})
        return jsonify({'error': 'Intervention record is not found'}), 400

    def delete_intervention(self, intervention_id):
        delete_int = Interventions().delete_one_intervention(intervention_id)
        if delete_int:
            return jsonify({
                "status": 200,
                "data": [{
                    "id": delete_int,
                    "message": "Intervention record has been deleted"
                }]
            })
        return jsonify({'error': 'Intervention record is not found'}), 400

    def admin_update_stat(self, intervention_id):
        data = request.get_json()
        status = data.get('status')
        valid_statuses = ['under investigation', 'rejected', 'resolved']
        if status not in valid_statuses:
            return jsonify({
                "status": 400,
                "message": "The new status should be either 'under investigation','rejected' or 'resolved "
            }), 400

        update_int = Interventions().admin_update_intervention_status( data['status'], intervention_id)
        if update_int:
            return jsonify({
                "status": 201,
                "data": [{
                    "id": update_int,
                    "message": "Updated intervention's status"
                }]
            })
        return jsonify({'error': 'Intervention record is not found'}), 400

    def update_intervention_location(self, redflag_id):
        pass

    def update_intervention_comment(self, redflag_id):
        pass
