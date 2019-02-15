from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity
from datetime import datetime
from restapi.models.database import DatabaseConnect


class RedflagController():

    def __init__(self):
        pass

    def create_redflag(self, incident_type):

        db = DatabaseConnect()
        data = request.get_json()
        incident_type = incident_type
        name = data.get("name")
        description = data.get("description")
        latitude = data.get("latitude")
        longitude = data.get("longitude")
        images = data.get("images")
        comment = data.get("comment")
        created_by = get_jwt_identity()



        incident_id = db.add_incident(incident_type= incident_type,
                                      name=data['name'],
                                      description= data['description'], 
                                      latitude=data['latitude'],
                                      longitude=data['longitude'],
                                      images=data['images'],
                                      comment=data['comment'],
                                      created_by=get_jwt_identity()
                                      
                                      )

        return jsonify({
            "status": 201,
            "data": [{
                "id": incident_id['incident_id'],
                "message": "Created incident record"}]
        }), 201

    def get_all_redflags(self):
        redflag = Redflags().get_all_redflag_records()
        if redflag:
            return jsonify({'status': 200,
                            'data': redflag})
        return jsonify({'error': 'red_flag is not found'}), 400

    def get_a_single_redflag(self, redflag_id):
        one_redflag = Redflags().get_one_redflag(redflag_id)
        if one_redflag:
            return jsonify({'status': 200,
                            'data': one_redflag})
        return jsonify({'error': 'Red_flag record is not found'}), 400

    def delete_redflag(self, redflag_id):
        del_int = Redflags().delete_one_redflag(redflag_id)
        if del_int:
            return jsonify({
                "status": 200,
                "data": [{
                    "id": del_int,
                    "message": "Red_flag record has been deleted"
                }]
            })
        return jsonify({'error': 'Redflag record is not found'}), 400

    def admin_update_stat(self, redflag_id):
        data = request.get_json()
        status = data.get('status')
        valid_statuses = ['under investigation', 'rejected', 'resolved']
        if status not in valid_statuses:
            return jsonify({
                "status": 400,
                "message": "The new status should be either 'under investigation','rejected' or 'resolved "
            }), 400

        update_int = Redflags().admin_update_redflag_status(
            data['status'], redflag_id)
        if update_int:
            return jsonify({
                "status": 201,
                "data": [{
                    "id": update_int,
                    "message": "Updated red_flag's status"
                }]
            }), 201
        return jsonify({'error': 'Redflag record is not found'}), 400

    def update_redflag_location(self, redflag_id):
        data = request.get_json()
        location = data['location']

        loc_int = Redflags().update_location(
            data['location'], redflag_id)
        if loc_int:
            return jsonify({
                "status": 201,
                "data": [{
                    "id": loc_int,
                    "message": "Updated red_flag's location"
                }]
            }), 201
        return jsonify({'error': 'Redflag record is not found'}), 400

    def update_redflag_comment(self, redflag_id):
        data = request.get_json()
        comment = data['comment']

        loc_int = Redflags().update_comment(
            data['comment'], redflag_id)
        if loc_int:
            return jsonify({
                "status": 201,
                "data": [{
                    "id": loc_int,
                    "message": "Updated redflag's comment"
                }]
            }), 201
        return jsonify({'error': 'Redflag record is not found'}), 400
