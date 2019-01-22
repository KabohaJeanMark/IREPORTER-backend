from flask import request, jsonify
from restapi.models.user_models import Users
import re




class UserController:

    def __init__(self):
        pass

    def create_users(self):
        users = Users()

        data = request.get_json()

        first_name = data.get("first_name")
        last_name = data.get("last_name")
        other_names = data.get("other_names")
        phone_number = str(data.get("phone_number"))
        user_name = data.get("user_name")
        str(user_name).replace(" ", "")
        email = data.get("email")
        password = data.get("password")
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
            
        users.register_users(username=data['username'],
                         password=data['password'],
                         email=data['email'],
                         phonenumber=data['phone_number'],
                         firstname= data['first_name'],
                         lastname= data['last_name'],
                         othernames= data['other_names'])

    def get_all_users(self):
        pass

    def get_a_single_user(self, user_id):
        pass