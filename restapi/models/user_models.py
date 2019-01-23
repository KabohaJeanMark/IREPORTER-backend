from datetime import datetime
from restapi.models.database import DatabaseConnect


class Users:
    def __init__(self):
        self.conn = DatabaseConnect()

    def register_users(self, username, email, password, firstname, lastname, othernames, phonenumber):
        """function that registers users """
        created_at = datetime.now()
        sql = "INSERT INTO users(\
                username, email, password, firstname,\
                lastname, othername, phonenumber, created_at)"\
              " VALUES('{}','{}','{}','{}','{}','{}','{}','{}')"\
              .format(username, email, password, firstname,
                      lastname, othernames, phonenumber, created_at)
        self.conn.cur.execute(sql)

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


