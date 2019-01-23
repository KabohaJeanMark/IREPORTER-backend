from datetime import datetime
from restapi.models.database import DatabaseConnect


class Interventions:
    def __init__(self):
        self.conn = DatabaseConnect()

    def add_intervention(self, location, status, images, videos, comment):
        status = 'draft'
        created_at = datetime.now()
        sql = """INSERT INTO interventions(\
                location, status, images, videos,\
                comment, created_at)\
                VALUES('{}','{}','{}','{}','{}','{}')"""\
              .format(location, status, images, videos, comment, created_at)
        self.conn.cur.execute(sql)

    def get_users_interventions(self):
        """function that fetches all interventions by a specific user"""
        sql = """ SELECT * FROM interventions ORDER BY created_at DESC """
        self.conn.cur.execute(sql)
        interventions = self.conn.cur.fetchall()
        return interventions
    
