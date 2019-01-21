from flask import request, jsonify
from datetime import datetime
from restapi.models.redflag_models import Redflags, BaseRedFlags, RedFlagsDb


IncidentsList = RedFlagsDb()


class RedFlagsController():

    def __init__(self):
        pass

    def create_redflag(self):
        if request.content_type != 'application/json':
            return jsonify({
                "status": "404",
                "message": "Content-type must be in json"
            })
        data = request.get_json()
        created_by = request.headers['user_id']
        incident_type = str(data.get("incident_type")).lower()
        status = "draft"
        redflag_id = len(IncidentsList.incident_list) + 1
        images = data.get("images")
        videos = data.get("videos")
        comment = data.get("comment")
        location = data.get("location")

        types_of_incidents = ['redflag', 'intervention']

        if not incident_type or not status or not images or not videos or not comment or not location:
            return jsonify({
                "status": "404",
                "message": "Required fields are missing. Either created_by, incident_type, images, videos, comment or location"
            })
        if incident_type not in types_of_incidents:
            return jsonify({
                "status": "404",
                "message": "the incident should be either a redflag or intervention"
            })

        if not isinstance(location, dict):
            return jsonify({
                "status": "404",
                "message": "location should be a dictionary of latitude and logitude coordinates"
            })
        if not isinstance(images, list) or not isinstance(videos, list):
            return jsonify({
                "status": "404",
                "message": "Images or videos should be in lists"
            })

        if not isinstance(comment, str):
            return jsonify({
                "status": "404",
                "message": "The comment should be of type string"
            })

        myredflag = Redflags(BaseRedFlags(
            created_by, incident_type), redflag_id, status, images, videos, comment, location)

        IncidentsList.add_redflag(myredflag)
        return jsonify({
            "status": 201,
            "data": [{
                "id": myredflag.redflag_id,
                "message": "Created red-flag record"

            }]

        })

    def get_all_redflags(self):
        return jsonify({
            "status": 200,
            "data": [redflag.to_json() for redflag in IncidentsList.incident_list]

        })

    def get_a_single_redflag(self, redflag_id):
        red = IncidentsList.get_one_redflag_by_id(redflag_id)
        if red:

            return jsonify({
                "status": 200,
                "data": red.to_json()
            })
        else:
            return jsonify({

                "status": 400,
                "message": "That red-flag id is not found"
            })

    def delete_redflag(self, redflag_id):
        red = IncidentsList.get_one_redflag_by_id(redflag_id)
        if red:
            IncidentsList.incident_list.remove(red)
            return jsonify({
                "status": 200,
                "message": "red-flag record has been deleted"
            })
        return jsonify({
            "status": 404,
            "message": "That red-flag id is not found"
        })

    def update_redflag_status(self, redflag_id):
        red = IncidentsList.get_one_redflag_by_id(redflag_id)
        if red:
            resp = request.get_json()
            stat = resp.get('status')
            print(stat)
            valid_statuses = ["under investigation", "rejected", "resolved"]
            if stat not in valid_statuses:
                return jsonify({
                    "status": 400,
                    "message": "The updated status has to be either 'under investigation' , 'resolved' or 'rejected' "
                })
            red.status = stat
            return jsonify({
                "status": 200,
                "id": red.redflag_id,
                "message": "Updated red-flag record's status"
            })

        return jsonify({
            "status": 404,
            "message": "That red-flag id is not found"
        })

    def update_redflag_location(self, redflag_id):
        red = IncidentsList.get_one_redflag_by_id(redflag_id)
        if red:
            if red.status != "draft":
                return jsonify({
                    "status": 400,
                    "message": "The admin has updated the status of the redflag. You can not edit the location."
                })
            red.location = request.get_json('location')
            return jsonify({
                "status": 200,
                "id": red.redflag_id,
                "message": "Updated red-flag record's location"
            })

        return jsonify({
            "status": 404,
            "message": "That red-flag id is not found"
        })

    def update_redflag_comment(self, redflag_id):
        red = IncidentsList.get_one_redflag_by_id(redflag_id)
        if red:
            if red.status != "draft":
                return jsonify({
                    "status": 400,
                    "message": "The admin has updated the status of the redflag. You can not edit the comment."
                })
            red.comment = request.get_json('comment')
            return jsonify({
                "status": 200,
                "id": red.redflag_id,
                "message": "Updated red-flag record's comment"
            })

        return jsonify({
            "status": 404,
            "message": "That red-flag id is not found"
        })
