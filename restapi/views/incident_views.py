from flask import Blueprint, jsonify, request
from restapi.controllers.incident_controllers import IncidentController
import jwt
from functools import wraps

bp = Blueprint("incident_views", __name__, url_prefix="/api/v1")

myIncident = IncidentController()


def protected(function):

    @wraps(function)
    def decorated(*args, **kwargs):

        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'error': 'token is missing!'}), 400
        try:
            data = jwt.decode(token, 'Secret Key')
            current_user = {
                user_id: data["user_id"],
                is_admin: data["admin"]
            }

        except:
            return jsonify({'error': 'token is invalid!'}), 400
        return function(current_user, *args, **kwargs)
    return decorated


@bp.route("/incidents/<incident_type>", methods=["POST"])
@protected
def add_incidents(incident_type, current_user):
    incident_type = incident_type
    return myIncident.create_incident(incident_type, current_user)


@bp.route("/incidents/<incident_type>", methods=["GET"])
@protected
def get_all_the_incidents(incident_type, current_user):
    incident_type = incident_type
    return myIncident.get_all_incidents(incident_type, current_user)


@bp.route("/incidents/<incident_type>/<int:incident_id>", methods=["GET"])
@protected
def get_incident(incident_type, incident_id, current_user):
    return myIncident.get_a_single_incident(incident_type, incident_id, current_user)


@bp.route("/incidents/<incident_type>/<int:incident_id>", methods=["DELETE"])
@protected
def delete_redflag(incident_type, incident_id, current_user):
    return myIncident.delete_incident(incident_type, incident_id, current_user)


@bp.route("/incidents/<incident_type>/<int:incident_id>/comment", methods=["PATCH"])
@protected
def update_incident_comment(incident_type, incident_id, current_user):
    return myIncident.update_incident_comment(incident_type, incident_id, current_user)


@bp.route("/incidents/<incident_type>/<int:incident_id>/location", methods=["PATCH"])
@protected
def update_incident_location(incident_type, incident_id, current_user):
    return myIncident.update_incident_location(incident_type, incident_id, current_user)


@bp.route("/incidents/<incident_type>/<int:incident_id>/status", methods=["PATCH"])
@protected
def update_incident_status(incident_type, incident_id, current_user):
    return myIncident.admin_update_stat(incident_type, incident_id, current_user)
