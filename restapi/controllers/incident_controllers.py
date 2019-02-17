from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity
from datetime import datetime
from restapi.models.database import DatabaseConnect


class IncidentController():

    def __init__(self):
        pass

    def create_incident(self, incident_type):

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

    def get_all_incidents(self,incident_type):
        redflag = DatabaseConnect().get_all_incident_records(incident_type)
        if redflag:
            return jsonify({'status': 200,
                            'data': redflag})
        return jsonify({'error': 'Incident record is not found'}), 400

    def get_a_single_incident(self, incident_type, incident_id):
        one_redflag = DatabaseConnect().get_one_incident(incident_type,incident_id)
        if one_redflag:
            return jsonify({'status': 200,
                            'data': one_redflag})
        return jsonify({'error': 'Incident record is not found'}), 400

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