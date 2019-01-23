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
                VALUES('{}','{}','{}','{}','{}','{}','{}') RETURNING intervention_id"""\
              .format(location, status, images, videos, comment, created_at, created_by)
        self.conn.cur.execute(sql)
        intervention = self.conn.cur.fetchone()
        return intervention

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
        intervention = self.conn.cur.fetchall()
        return intervention

    def get_one_intervention(self, intervention_id):
        """function that fetches one interventions"""
        sql = "SELECT * FROM interventions WHERE intervention_id='{}'".format(
            intervention_id)+"ORDER BY created_at DESC"
        self.conn.cur.execute(sql)
        interventions = self.conn.cur.fetchone()
        return interventions

    def delete_one_intervention(self, intervention_id):
        """ function that deletes an intervention record"""
        delete_query = "DELETE FROM interventions WHERE intervention_id = '{}'".format(
            intervention_id)
        deleted_interv = intervention_id
        self.conn.cur.execute(delete_query)
        return deleted_interv

    def admin_update_intervention_status(self, status, intervention_id):
        """function that enables the admin to update the intervention status"""
        sql = "UPDATE interventions SET status='{}'".format(status) + " WHERE intervention_id='{}'".format(intervention_id)
        self.conn.cur.execute(sql)
        stat_id = intervention_id
        return stat_id
