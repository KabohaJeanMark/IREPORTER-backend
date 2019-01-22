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
                lastname, othernames, phonenumber, create_at)"\
              " VALUES('{}','{}','{}','{}','{}','{}','{}','{}')"\
              .format(username, email, password, phonenumber, firstname, lastname, othernames, created_at)
        self.conn.cur.execute(sql)

