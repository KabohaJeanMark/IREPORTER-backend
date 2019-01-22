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
