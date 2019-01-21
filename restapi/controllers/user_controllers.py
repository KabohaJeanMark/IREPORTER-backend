from flask import request, jsonify
from restapi.models.user_models import Users, BaseUsers, UsersDB
import re

UsersList = UsersDB()


class UserController:

    def __init__(self):
        pass

    def create_users(self):
        data = request.get_json()

        first_name = data.get("first_name")
        last_name = data.get("last_name")
        other_names = data.get("other_names")
        phone_number = str(data.get("phone_number"))
        user_id = len(UsersList.user_list) + 1
        user_name = data.get("user_name")
        str(user_name).replace(" ", "")
        email = data.get("email")
        is_admin = False


        if not isinstance(first_name, str) or not isinstance(last_name, str) or not isinstance(other_names,str):
            return jsonify({
                "status": "404",
                "message": "All the names have to be of type string"
            })

        if len(phone_number) < 10:
            return jsonify({
                "status": "404",
                "message": "The phone number should be a string of atleast 10 digits"
            })
        if not re.match("[0-9]", phone_number):
            return jsonify({
                "status": "404",
                "message": "The phone number should be a string of only digits from 0 to 9"
            })
        if not re.match(r"[^@.]+@[A-Za-z]+\.[a-z]+", email):
            return jsonify({
                "status": "404",
                "message": "The email address is in the wrong format"
            })
            

        myUser = Users(BaseUsers(
            first_name, last_name, other_names, phone_number), user_id, email, user_name, is_admin)

        UsersList.add_user(myUser)
        return jsonify({
            "status": 201,
            "data": [{
                "id": myUser.user_id,
                "message": "Created new user"
            }]
        })

    def get_all_users(self):
        return jsonify({
            "status": 200,
            "data": [user.to_json() for user in UsersList.user_list]
        })

    def get_a_single_user(self, user_id):
        user = UsersList.get_one_user_by_id(user_id)
        if user:
            return jsonify({
                "status": 200,
                "data": user.to_json()
            })
        else:
            return jsonify({
                "status": 404,
                "message": "That user id is not found"
            })
