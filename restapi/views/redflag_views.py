from flask import Blueprint, jsonify
from restapi.controllers.redflag_controllers import InterventionsController


BPrint = Blueprint("redflag_views", __name__, url_prefix="/api/v1")

myIntervention = InterventionsController()


@BPrint.route("/")
def index():
    return jsonify({"Message": "Welcome to Ireporter"})


@BPrint.route("/interventions", methods=["POST"])
def add_intervention():
    return myIntervention.create_intervention(), 201


@BPrint.route("/interventions", methods=["GET"])
def get_all_user_interventions():
    return myIntervention.get_all_interventions()


@BPrint.route("/redflags/<int:redflag_id>", methods=["GET"])
def get_redflag(redflag_id):
    pass


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
