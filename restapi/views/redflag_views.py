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
    return myIntervention.create_intervention(), 201


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

@BPrint.route("/redflags/<int:redflag_id>", methods=["DELETE"])
def delete_redflag(redflag_id):
    pass


@BPrint.route("/redflags/<int:redflag_id>/location", methods=["PATCH"])
def update_redflags_location(redflag_id):
    pass


@BPrint.route("/redflags/<int:redflag_id>/comment", methods=["PATCH"])
def update_redflags_comment(redflag_id):
    pass


@BPrint.route("/redflags/<int:redflag_id>/status", methods=["PATCH"])
def update_redflags_status(redflag_id):
    pass
