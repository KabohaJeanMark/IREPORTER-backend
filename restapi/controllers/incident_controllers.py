from flask import request, jsonify
from datetime import datetime
from restapi.models.database import DatabaseConnect


class IncidentController():

    def __init__(self):
        pass

    def create_incident(self,current_user,incident_type):
# first arg is current_user and 2nd is incident_type
        db = DatabaseConnect()
        data = request.get_json()

        incident_id = db.add_incident(
                                      incident_type=incident_type,
                                      name=data['name'],
                                      description=data['description'],
                                      location=data['location'],
                                      images=data['images'],
                                      comment=data['comment'],
                                      created_by=current_user['user_id']
                                      )

        return jsonify({
            "status": 201,
            "data": [{
                "id": incident_id['incident_id'],
                "message": "Created incident record"}]
        }), 201

    def get_all_incidents(self, current_user, incident_type):
        redflag = DatabaseConnect().get_all_incident_records(current_user['user_id'], incident_type)
        if redflag:
            return jsonify({'status': 200,
                            'data': redflag})
        return jsonify({'error': 'Incident record is not found'}), 400

    def get_a_single_incident(self, current_user, incident_type, incident_id):
        one_redflag = DatabaseConnect().get_one_incident(current_user['user_id'],incident_type, incident_id)
        if one_redflag:
            return jsonify({'status': 200,
                            'data': one_redflag})
        return jsonify({'error': 'Incident record is not found'}), 400

    def delete_incident(self,current_user, incident_type, incident_id):
        del_int = DatabaseConnect().delete_one_incident(current_user['user_id'],incident_type, incident_id)
        if del_int:
            return jsonify({
                "status": 200,
                "data": [{
                    "id": del_int,
                    "message": "Incident record has been deleted"
                }]
            })
        return jsonify({'error': 'Incident record is not found'}), 400

    def update_incident_location(self, current_user, incident_type, incident_id):
        data = request.get_json()

        loc_int = DatabaseConnect().update_location( current_user['user_id'],
            data['location'], incident_type, incident_id)
        if loc_int:
            return jsonify({
                "status": 201,
                "data": [{
                    "id": loc_int,
                    "message": "Updated incident's location"
                }]
            }), 201
        return jsonify({'error': 'Incident record is not found'}), 400

    def update_incident_comment(self, current_user, incident_type, incident_id):
        data = request.get_json()

        loc_int = DatabaseConnect().update_comment(current_user['user_id'],
            data['comment'], incident_type, incident_id)
        if loc_int:
            return jsonify({
                "status": 201,
                "data": [{
                    "id": loc_int,
                    "message": "Updated incident's comment"
                }]
            }), 201
        return jsonify({'error': 'Incident record is not found'}), 400

    # def admin_update_stat(self, current_user ,incident_type, incident_id):
    #     #return jsonify (current_user)
    #     if current_user['isadmin']:

    #         data = request.get_json()
    #         status = data.get('status')
    #         valid_statuses = ['under investigation', 'rejected', 'resolved']
    #         if status not in valid_statuses:
    #             return jsonify({
    #                 "status": 400,
    #                 "message": "The new status should be either 'under investigation','rejected' or 'resolved "
    #             }), 400

            #  update_int = DatabaseConnect().admin_update_status(
            #      data['status'], incident_type, incident_id)
            #  if update_int:
            #     return jsonify({
            #         "status": 201,
            #         "data": [{
            #             "id": update_int,
            #             "message": "Updated incident's status"
            #         }]
            #     }), 201
            # return jsonify({'error': 'Incident record is not found'}), 400
    #     return jsonify({'error':'This route is only accessible for the administrators'}), 400

    def admin_update_stat(self, incident_id):
        data = request.get_json()
        status = data.get('status')
        valid_statuses = ['under investigation', 'rejected', 'resolved']
        if status not in valid_statuses:
            return jsonify({
                "status": 400,
                "message": "The new status should be either 'under investigation','rejected' or 'resolved "
                }), 400
        update_int = DatabaseConnect().admin_update_status(
                 data['status'],incident_id)
        if update_int:
            return jsonify({
                "status": 201,
                "data": [{
                    "id": update_int,
                    "message": "Updated incident's status"
            }]
        }), 201
        return jsonify({'error': 'Incident record is not found'}), 400



    def get_all_the_incidents(self):
        incident = DatabaseConnect().get_all_inc_records()
        if incident:
            return jsonify({'status': 200,
                            'data': incident})
        return jsonify({'error': 'Incident record is not found'}), 400
