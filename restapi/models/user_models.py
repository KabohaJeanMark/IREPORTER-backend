import datetime


class BaseUsers:
    def __init__(self, first_name, last_name, other_names, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.other_names = other_names
        self.phone_number = phone_number


class Users:
    def __init__(self, base, user_id, email, user_name, is_admin):
        self.base = base
        self.user_id = user_id
        self.email = email
        self.user_name = user_name
        self.registered = datetime.datetime.now()
        self.is_admin = is_admin

    def to_json(self):
        """Creates a json representation of a user instance """
        return {
            "id": self.user_id,
            "firstname": self.base.first_name,
            "lastname": self.base.last_name,
            "othernames": self.base.other_names,
            "phonenumber": self.base.phone_number,
            "email": self.email,
            "username": self.user_name,
            "registered": self.registered,
            "isadmin": self.is_admin
        }


class UsersDB:
    def __init__(self):
        self.user_list = []

    def add_user(self, user):
        self.user_list.append(user)

    def get_users(self):
        return self.user_list

    def get_one_user_by_id(self, user_id):
        for user in self.user_list:
            if user.user_id == user_id:
                return user
        return None
