from flask import Blueprint, jsonify
from restapi.controllers.redflag_controllers import RedFlagsController


BPrint = Blueprint("redflag_views", __name__, url_prefix="/api/v1")

myRedflag = RedFlagsController()


@BPrint.route("/")
def index():
    return jsonify({"Message": "Welcome to Ireporter"})


@BPrint.route("/redflags", methods=["POST"])
def add_redflag():
    return myRedflag.create_redflag(), 201


@BPrint.route("/redflags", methods=["GET"])
def get_redflags():
    return myRedflag.get_all_redflags(), 200


@BPrint.route("/redflags/<int:redflag_id>", methods=["GET"])
def get_redflag(redflag_id):
    return myRedflag.get_a_single_redflag(redflag_id), 200


@BPrint.route("/redflags/<int:redflag_id>", methods=["DELETE"])
def delete_redflag(redflag_id):
    return myRedflag.delete_redflag(redflag_id), 200


@BPrint.route("/redflags/<int:redflag_id>/location", methods=["PATCH"])
def update_redflags_location(redflag_id):
    return myRedflag.update_redflag_location(redflag_id), 200


@BPrint.route("/redflags/<int:redflag_id>/comment", methods=["PATCH"])
def update_redflags_comment(redflag_id):
    return myRedflag.update_redflag_comment(redflag_id), 200


@BPrint.route("/redflags/<int:redflag_id>/status", methods=["PATCH"])
def update_redflags_status(redflag_id):
    return myRedflag.update_redflag_status(redflag_id), 200
