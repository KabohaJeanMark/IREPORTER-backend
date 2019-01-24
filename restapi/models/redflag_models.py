from datetime import datetime
from restapi.models.database import DatabaseConnect


class Redflags:
    def __init__(self):
        self.conn = DatabaseConnect()

    def add_redflag(self, location, images, videos, comment, created_by):
        status = 'draft'
        created_at = datetime.now()
        sql = """INSERT INTO redflags(\
                location, images, videos,\
                comment, created_at, user_id)\
                VALUES('{}','{}','{}','{}','{}','{}') RETURNING redflag_id"""\
              .format(location, images, videos, comment, created_at, created_by)
        self.conn.cur.execute(sql)
        redflag = self.conn.cur.fetchone()
        return redflag

    def get_all_redflag_records(self):
        """function that fetches all redflags"""
        sql = """ SELECT * FROM redflags ORDER BY created_at DESC """
        self.conn.cur.execute(sql)
        redflags = self.conn.cur.fetchall()
        return redflags

    def get_one_redflag(self, redflag_id):
        """function that fetches one redflag"""
        sql = "SELECT * FROM redflags WHERE redflag_id='{}'".format(
            redflag_id)+"ORDER BY created_at DESC"
        self.conn.cur.execute(sql)
        redflags = self.conn.cur.fetchone()
        return redflags

    def delete_one_redflag(self, redflag_id):
        """ function that deletes a redflag record"""
        delete_query = "DELETE FROM redflags WHERE redflag_id = '{}'".format(
            redflag_id)
        deleted_interv = redflag_id
        self.conn.cur.execute(delete_query)
        return deleted_interv

    def admin_update_redflag_status(self, status, redflag_id):
        """function that enables the admin to update the redflag status"""
        sql = "UPDATE redflags SET status='{}'".format(status) + " WHERE redflag_id='{}'".format(redflag_id)
        self.conn.cur.execute(sql)
        stat_id = redflag_id
        return stat_id

    def update_location(self, location, redflag_id):
        """function that updates the location"""
        sql = "UPDATE redflags SET location='{}'".format(location) + " WHERE redflag_id='{}'".format(redflag_id)
        self.conn.cur.execute(sql)
        loc_id = redflag_id
        return loc_id       

    def update_comment(self, comment, redflag_id):
        """function that updates the comment"""
        sql = "UPDATE redflags SET comment='{}'".format(comment) + " WHERE redflag_id='{}'".format(redflag_id)
        self.conn.cur.execute(sql)
        comm_id = redflag_id
        return comm_id         