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

@BP.route("/auth/admin", methods = ["POST"])
def admin_sign_up():
    return myUser.admin_login()
