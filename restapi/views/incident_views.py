from flask import Blueprint, jsonify
from restapi.controllers.incident_controllers import IncidentController
from flask_jwt_extended import jwt_required

bp = Blueprint("incident_views", __name__, url_prefix="/api/v1")

myIncident = IncidentController()


@bp.route("/incidents/<incident_type>", methods=["POST"])
@jwt_required
def add_incidents(incident_type):
    incident_type = incident_type
    return myIncident.create_incident(incident_type)


@jwt_required
@bp.route("/incidents/<incident_type>", methods=["GET"])
def get_all_the_incidents(incident_type):
    incident_type = incident_type
    return myIncident.get_all_incidents(incident_type)


@jwt_required
@bp.route("/incidents/<incident_type>/<int:incident_id>", methods=["GET"])
def get_incident(incident_type, incident_id):
    return myIncident.get_a_single_incident(incident_type, incident_id)


@jwt_required
@bp.route("/incidents/<incident_type>/<int:incident_id>", methods=["DELETE"])
def delete_redflag(incident_type, incident_id):
    return myIncident.delete_incident(incident_type, incident_id)


@jwt_required
@bp.route("/incidents/<incident_type>/<int:incident_id>/comment", methods=["PATCH"])
def update_incident_comment(incident_type, incident_id):
    return myIncident.update_incident_comment(incident_type, incident_id)


@jwt_required
@bp.route("/incidents/<incident_type>/<int:incident_id>/location", methods=["PATCH"])
def update_incident_location(incident_type, incident_id):
    return myIncident.update_incident_location(incident_type, incident_id)


@jwt_required
@bp.route("/incidents/<incident_type>/<int:incident_id>/status", methods=["PATCH"])
def update_incident_status(incident_type, incident_id):
    return myIncident.admin_update_stat(incident_type, incident_id)
