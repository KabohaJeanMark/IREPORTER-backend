from datetime import datetime
from restapi.models.database import DatabaseConnect


class Interventions:
    def __init__(self):
        self.conn = DatabaseConnect()

    def create_intervention(self, location, status, images, videos, comment, created_by):
        status = 'draft'
        created_at = datetime.now()
        sql = """INSERT INTO interventions(\
                location, status, images, videos,\
                comment, created_by ,created_at)"\
              " VALUES('{}','{}','{}','{}','{}','{}','{}')RETURNING user_id"""\
              .format(location, status, images, videos, comment, created_by, created_at)
        self.conn.cur.execute(sql)
        

    def get_latest_record(self):
        pass
