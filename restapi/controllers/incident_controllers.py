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