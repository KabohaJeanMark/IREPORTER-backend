from flask import Blueprint, jsonify
from restapi.controllers.redflag_controllers import RedflagController
from flask_jwt_extended import jwt_required

bp = Blueprint("redflag_views", __name__, url_prefix="/api/v1")

myRedflag = RedflagController()


@bp.route("/redflags", methods=["POST"])
@jwt_required
def add_redflag():
    return myRedflag.create_redflag()


@jwt_required
@bp.route("/redflags", methods=["GET"])
def get_all_the_redflags():
    return myRedflag.get_all_redflags()


@jwt_required
@bp.route("/redflags/<int:redflag_id>", methods=["GET"])
def get_redflag(redflag_id):
    return myRedflag.get_a_single_redflag(redflag_id)


@bp.route("/redflags/<int:redflag_id>", methods=["DELETE"])
def delete_redflag(redflag_id):
    return myRedflag.delete_redflag(redflag_id)


@bp.route("/redflags/<int:redflag_id>/location", methods=["PATCH"])
def update_redflag_location(redflag_id):
    return myRedflag.update_redflag_location(redflag_id)


@bp.route("/redflags/<int:redflag_id>/comment", methods=["PATCH"])
def update_redflags_comment(redflag_id):
    return myRedflag.update_redflag_comment(redflag_id)


@bp.route("/redflags/<int:redflag_id>/status", methods=["PATCH"])
def update_redflag_status(redflag_id):
    return myRedflag.admin_update_stat(redflag_id)
