from flask import Blueprint, jsonify
from restapi.controllers.redflag_controllers import InterventionsController
from flask_jwt_extended import jwt_required

BPrint = Blueprint("redflag_views", __name__, url_prefix="/api/v1")

myIntervention = InterventionsController()


@BPrint.route("/")
def index():
    return jsonify({"Message": "Welcome to Ireporter"})


@BPrint.route("/interventions", methods=["POST"])
@jwt_required
def add_intervention():
    return myIntervention.create_intervention()


@BPrint.route("/interventions", methods=["GET"])
def get_all_the_interventions():
    return myIntervention.get_all_interventions()

@jwt_required
@BPrint.route("user/interventions/<int:user_id>", methods=["GET"])
def get_all_a_users_interventions(user_id):
    return myIntervention.get_all_a_users_interventions(user_id)

@jwt_required
@BPrint.route("/interventions/<int:intervention_id>", methods=["GET"])
def get_intervention(intervention_id):
    return myIntervention.get_a_single_intervention(intervention_id)  

@BPrint.route("/interventions/<int:intervention_id>", methods=["DELETE"])
def delete_intervention(intervention_id):
    return myIntervention.delete_intervention(intervention_id)

@BPrint.route("/interventions/<int:intervention_id>/location", methods=["PATCH"])
def update_interventions_location(intervention_id):
    return myIntervention.update_intervention_location(intervention_id)


@BPrint.route("/interventions/<int:intervention_id>/comment", methods=["PATCH"])
def update_interventions_comment(intervention_id):
    return myIntervention.update_intervention_comment(intervention_id)


@BPrint.route("/interventions/<int:intervention_id>/status", methods=["PATCH"])
def update_intervention_status(intervention_id):
    return myIntervention.admin_update_stat(intervention_id)
