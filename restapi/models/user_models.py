from datetime import datetime
from restapi.models.database import DatabaseConnect
from flask import jsonify


class Users:
    def __init__(self):
        self.conn = DatabaseConnect()

    def register_users(self, username, email, password, firstname, lastname, othernames, phonenumber, isadmin):
        """function that registers users """
        created_at = datetime.now()
        sql = "INSERT INTO users(\
                username, email, password, firstname,\
                lastname, othername, phonenumber, admin, created_at)"\
              " VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}') RETURNING user_id "\
              .format(username, email, password, firstname,
                      lastname, othernames, phonenumber, isadmin, created_at)
        self.conn.cur.execute(sql)
        user = self.conn.cur.fetchone()
        return user

    def check_email_exists(self, email):
        """function that checks and validates unique email in db"""
        sql_email = "SELECT* FROM users WHERE email='{}'".format(
            email)
        self.conn.cur.execute(sql_email)
        row = self.conn.cur.fetchone()
        return row

    def check_username_exists(self, username):
        """function that checks and validates unique username in db"""
        sql_username = "SELECT* FROM users WHERE username='{}'".format(
            username)
        self.conn.cur.execute(sql_username)
        row = self.conn.cur.fetchone()
        return row

    def check_login_user(self, username, password):
        """login user"""
        sql = "SELECT * FROM users WHERE username='{}'".format(
            username) + "and password='{}'".format(password)
        self.conn.cur.execute(sql)
        users = self.conn.cur.fetchone()
        return users

    def get_current_user(self, user_id):
        sql = "SELECT * FROM users WHERE username='{}'".format(user_id)
        self.conn.cur.execute(sql)
        user = self.conn.cur.fetchone()
        if user:
            return user
        return False

    def get_user(self, username):
        query = "SELECT * FROM users WHERE username='{}'".format('username')
        self.conn.cur.execute(query)
        user = self.conn.cur.fetchone()
        if user:
            return user
        return False


