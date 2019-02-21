from flask import Blueprint, jsonify
from restapi.controllers.user_controllers import UserController


BP = Blueprint("user_views", __name__, url_prefix="/api/v1")

myUser = UserController()


@BP.route("/", methods=["GET"])
def home_page():
    return jsonify({"Message": "Welcome to Ireporter"})


@BP.route("/auth/signup", methods=["POST"])
def add_user():
    return myUser.create_users()


@BP.route("/auth/login", methods=["POST"])
def sign_in():
    return myUser.login_user()


@BP.route("/admin/users", methods=["GET"])
def get_users():
    return myUser.get_all_users()


@BP.route("/admin/<int:user_id>/status", methods=["PATCH"])
def admin_update_user(user_id):
    return myUser.admin_make_user_admin(user_id)
