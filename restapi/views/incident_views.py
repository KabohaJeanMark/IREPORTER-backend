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
            #current_user = {"user_id": data['user_id'],"is_admin": data['admin']}
            current_user = data
            #current_user = data['user_id']

        except:
            return jsonify({'error': 'token is invalid!'}), 400
        return function(current_user, *args, **kwargs)
    return decorated


@bp.route("/incidents/<incident_type>", methods=["POST"])
@protected
def add_incidents(current_user, incident_type):
    return myIncident.create_incident(current_user,incident_type)

@bp.route("/incidents", methods =["GET"])
def get_all_incidents():
    return myIncident.get_all_the_incidents()


@bp.route("/incidents/<incident_type>", methods=["GET"])
@protected
def get_all_the_incidents(current_user,incident_type):
    incident_type = incident_type
    return myIncident.get_all_incidents(current_user,incident_type)


@bp.route("/incidents/<incident_type>/<int:incident_id>", methods=["GET"])
@protected
def get_incident( current_user,incident_type, incident_id,):
    return myIncident.get_a_single_incident( current_user,incident_type, incident_id)


@bp.route("/incidents/<incident_type>/<int:incident_id>", methods=["DELETE"])
@protected
def delete_incident( current_user,incident_type, incident_id):
    return myIncident.delete_incident(current_user,incident_type, incident_id)


@bp.route("/incidents/<incident_type>/<int:incident_id>/comment", methods=["PATCH"])
@protected
def update_incident_comment(current_user,incident_type, incident_id):
    return myIncident.update_incident_comment(current_user,incident_type, incident_id)


@bp.route("/incidents/<incident_type>/<int:incident_id>/location", methods=["PATCH"])
@protected
def update_incident_location(current_user,incident_type, incident_id):
    return myIncident.update_incident_location(current_user,incident_type, incident_id)


# @bp.route("/incidents/<incident_type>/<int:incident_id>/status", methods=["PATCH"])
# @protected
# def update_incident_status(current_user,incident_type, incident_id):
#     return myIncident.admin_update_stat(current_user,incident_type, incident_id)

@bp.route("/incidents/<int:incident_id>/status", methods=["PATCH"])
def admin_update_status(incident_id):
    return myIncident.admin_update_stat(incident_id)

