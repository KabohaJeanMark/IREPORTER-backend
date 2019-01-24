from datetime import datetime
from restapi.models.database import DatabaseConnect
from flask import jsonify

class Users:
    def __init__(self):
        self.conn = DatabaseConnect()

    def register_users(self, username, email, password, firstname, lastname, othernames, phonenumber):
        """function that registers users """
        created_at = datetime.now()
        sql = "INSERT INTO users(\
                username, email, password, firstname,\
                lastname, othername, phonenumber, created_at)"\
              " VALUES('{}','{}','{}','{}','{}','{}','{}','{}') RETURNING username "\
              .format(username, email, password, firstname,
                      lastname, othernames, phonenumber, created_at)
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
        sql = "SELECT * FROM users WHERE username='{}'".format(username) + "and password='{}'".format(password)
        self.conn.cur.execute(sql)
        users = self.conn.cur.fetchone()
        return users
    def create_admin_in_db(self):
        """function to create a default administrator"""
        created_at = datetime.now()
        sql = "INSERT INTO users(\
                username, email, password, firstname,\
                lastname, othername, phonenumber, created_at)"\
              " VALUES('admin', 'admin256@gmail.com', 'admin123','jean','mark','kairumba','0758638747','{}'".format(created_at)
        self.conn.cur.execute(sql)
        
    def get_user(self, user_id):
        """checks whether the current user is an admin"""
        sql = "SELECT * FROM users WHERE user_id='{}'".format(user_id)
        self.conn.cur.execute(sql)
        role = self.conn.cur.fetchone()
        return role


