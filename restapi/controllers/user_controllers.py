from flask import request, jsonify
from flask_jwt_extended import create_access_token
from restapi.models.user_models import Users
import datetime


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
        user_exist = users.check_username_exists(username=data['username'])
        if user_exist:
            return jsonify({
                "status": 400,
                "message": "That username already exists"
            })
        email_taken = users.check_email_exists(email=data['email'])
        if email_taken:
            return jsonify({
                "status": 400,
                "message": "That email is already taken"
            })

        new = users.register_users(username=data['username'],
                                   email=data['email'],
                                   password=data['password'],
                                   firstname=data['first_name'],
                                   lastname=data['last_name'],
                                   othernames=data['othernames'],
                                   phonenumber=data['phone_number'])
        return jsonify({
            "status": 201,
            "data": new,
            "message": "User has been succesfully created"
        })

    def login_user(self):
        """endpoint for logging in  users"""
        data = request.get_json()
        login = Users()
        username = data.get("username")
        password = data.get("password")


        valid_user = login.check_login_user(
            data['username'], data['password'])
        if valid_user:
            exp = datetime.timedelta(days = 1)
            token = create_access_token(username, expires_delta= exp )

            return jsonify({
                "message": "successfully logged in",
                "token": token
            })


        return jsonify({
            "status": 400,
            "message": "Please enter valid username and password"}) , 400

    def get_all_users(self):
        pass

    def get_a_single_user(self, user_id):
        pass
