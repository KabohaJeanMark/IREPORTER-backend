import re
import jwt
import datetime
from flask import request, jsonify
from restapi.models.database import DatabaseConnect
from restapi.utilities.validations import check_format_of_phone_number, check_unfilled_fields,\
    check_length_of_fields, check_proper_email_format, check_special_characters


class UserController:

    def __init__(self):
        self.database = DatabaseConnect()

    def create_users(self):
        data = request.get_json()
        username = data['username']
        last_name =data['last_name']
        othernames = data['othernames']
        phone_number = data['phone_number']
        email = data['email']
        password = data['password']
        if not data:
            return jsonify({
                "status": "400",
                "message": "A key is missing"
            })
        if check_unfilled_fields(data['username'], data['last_name'], data['othernames'],
                                 data['phone_number'], data['email'], data['password']):
            return jsonify({
                "status": "400",
                "message": "Please fill in a missing field"
            }), 400
        if check_length_of_fields(data['username'], data['last_name'], data['othernames']):
            return jsonify({
                "status": "400",
                "message": "The names should have a length of at most 30 characters"
            }), 400
        if check_special_characters(data['username']):
            return jsonify({
                "status": "400",
                "message": "The username should be a normal string without special characters"
            }),

        if len(data['phone_number']) < 10:
            return jsonify({
                "status": "400",
                "message": "The phone number should be a string of atleast 10 digits"
            }), 400

        if not check_proper_email_format(data['email']):
            return jsonify({
                "status": "400",
                "message": "The email address is in the wrong format"
            }), 400
        user_exist = self.database.check_username_exists(username=data['username'])
        if user_exist:
            return jsonify({
                "status": 400,
                "message": "That username already exists"
            }), 400
        email_taken = self.database.check_email_exists(email=data['email'])
        if email_taken:
            return jsonify({
                "status": 400,
                "message": "That email is already taken"
            }), 400

        reg_user_id = self.database.register_users(username=data['username'],
                                           email=data['email'],
                                           password=data['password'],
                                           firstname=data['first_name'],
                                           lastname=data['last_name'],
                                           othernames=data['othernames'],
                                           phonenumber=data['phone_number']
                                           
                                           )

        return jsonify({
            "status": 201,
            "data": [{
                "id": reg_user_id,
                "message": "User has been succesfully created"
            }]
        }), 201

    def login_user(self):
        """endpoint for logging in  users"""
        data = request.get_json()

        

        user_login = self.database.check_login_user(data['username'], data['password'])

        if user_login:
            user = self.database.get_user(data['username'])
            if user:
                payload = {
                    'user_id': user['user_id'],
                    'first_name': user['firstname'],
                    'last_name': user['lastname'],
                    'othernames': user['othername'],
                    'password': user['password'],
                    'email': user['email'],
                    'phone_number': user['phonenumber'],
                    'username': user['username'],
                    'isadmin': user['admin'],
                    'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
                }

                token = jwt.encode(payload, 'Secret Key')

                return jsonify({
                    "message": "successfully logged in",
                    "token": token.decode('UTF-8')
                }), 200
            return jsonify({
                "status": 400,
                "message":"That user doesn't exist"
            })
        return jsonify({
            "status": 400,
            "message": "Please enter valid username and password"}), 400
