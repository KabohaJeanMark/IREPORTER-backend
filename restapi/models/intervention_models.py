from datetime import datetime
from restapi.models.database import DatabaseConnect


class Interventions:
    def __init__(self):
        self.conn = DatabaseConnect()

    def add_intervention(self, name, description,latitude, longitude, images, comment, created_by):
        created_at = datetime.now()
        sql = """INSERT INTO interventions(name, \
                 description,latitude,\
                longitude,images, comment,\
                created_at, user_id)\
                VALUES('{}','{}','{}','{}','{}','{}','{}','{}') RETURNING intervention_id"""\
              .format(name, description,latitude, longitude, images, comment, created_at, created_by)
        self.conn.cur.execute(sql)
        incident = self.conn.cur.fetchone()
        return incident

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

    def update_location(self, latitude, longitude, incident_type, incident_id):
        """function that updates the location"""
        sql = "UPDATE interventions SET latitude='{}' AND longitude='{}'".format(latitude, longitude) + " WHERE incident_type='{}' AND incident_id='{}'".format(incident_type,incident_id)
        self.conn.cur.execute(sql)
        loc_id = incident_id
        return loc_id       

    def update_comment(self, comment, incident_type, incident_id):
        """function that updates the comment"""
        sql = "UPDATE interventions SET comment='{}'".format(comment) + " WHERE incident_type ='{}' AND incident_id='{}'".format(incident_type,incident_id)
        self.conn.cur.execute(sql)
        comm_id = incident_id
        return comm_id         