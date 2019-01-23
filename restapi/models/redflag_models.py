from datetime import datetime
from restapi.models.database import DatabaseConnect


class Interventions:
    def __init__(self):
        self.conn = DatabaseConnect()

    def add_intervention(self, location, status, images, videos, comment, created_by):
        status = 'draft'
        created_at = datetime.now()
        sql = """INSERT INTO interventions(\
                location, status, images, videos,\
                comment, created_at, user_id)\
                VALUES('{}','{}','{}','{}','{}','{}','{}')"""\
              .format(location, status, images, videos, comment, created_at, created_by)
        self.conn.cur.execute(sql)

    def get_all_intervention_records(self):
        """function that fetches all interventions"""
        sql = """ SELECT * FROM interventions ORDER BY created_at DESC """
        self.conn.cur.execute(sql)
        interventions = self.conn.cur.fetchall()
        return interventions

    def get_all_interventions_by_specific_user(self, user_id):
        """function that fetches all interventions"""
        sql = "SELECT * FROM interventions WHERE user_id='{}'".format(
            user_id)+"ORDER BY created_at DESC"
        self.conn.cur.execute(sql)
        interventions = self.conn.cur.fetchall()
        return interventions

    def get_one_intervention(self):
        pass
