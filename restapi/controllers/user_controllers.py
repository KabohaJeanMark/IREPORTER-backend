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
        othernames = data.get("othernames")
        phone_number = str(data.get("phone_number"))
        user_name = data.get("username")
        str(user_name).replace(" ", "")
        email = data.get("email")
        password = data.get("password")

        user_postman_inputs = [first_name, last_name,
                               othernames, phone_number, user_name, email, password]
        for value in user_postman_inputs:
            if not value:
                return jsonify({
                    "status": "400",
                    "message": "A field value is missing"
                })
        if not data:
            return jsonify({
                "status": "400",
                "message": "A key is missing"
            })

        if not isinstance(first_name, str) or not isinstance(last_name, str) or not isinstance(othernames, str):
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
                             email=data['email'],
                             password=data['password'],
                             firstname=data['first_name'],
                             lastname=data['last_name'],
                             othernames=data['othernames'],
                             phonenumber=data['phone_number'],)
        return jsonify({
            "data": 201,
            "message": "User has been succesfully created"
        })

    def get_all_users(self):
        pass

    def get_a_single_user(self, user_id):
        pass
