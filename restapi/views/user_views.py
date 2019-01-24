from flask import Blueprint, jsonify
from restapi.controllers.user_controllers import UserController
from flask_jwt_extended import jwt_required

BP = Blueprint("user_views", __name__, url_prefix="/api/v1")

myUser = UserController()


@BP.route("/auth/signup", methods=["POST"])
def add_user():
    return myUser.create_users()


@BP.route("/auth/login", methods=["POST"])
def sign_in():
    return myUser.login_user()


@BP.route("/users", methods=["GET"])
def get_users():
    return myUser.get_all_users()


@BP.route("/users/<int:user_id>", methods=["GET"])
def get_one_user_by_id(user_id):
    return myUser.get_a_single_user(user_id)
