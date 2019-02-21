import psycopg2
from psycopg2 import extras
import os
from datetime import datetime


class DatabaseConnect:
    """class that establishes database connection, creates various tables and drops the tables """

    def __init__(self):

        if os.getenv('DB_NAME') == "testdb":
            self.dbname = "testdb"
            self.user = "postgres"
            self.password = ""
            self.host = "127.0.0.1"
        elif os.getenv('DB_NAME') == "ireporter":
            self.dbname = "ireporter"
            self.user = "postgres"
            self.password = ""
            self.host = "127.0.0.1"
        else:
            self.dbname = "ddo76jqcvdgpp6"
            self.user = "iahxwhjlgkymau"
            self.password = "86ca7ea32a682d6e997410bd6ce1093093a51f2b3ba4ba9c9bb5a2efb0598e41"
            self.host = "ec2-54-221-253-228.compute-1.amazonaws.com"
        
        try:
            self.connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                host=self.host,
                password=self.password,
                port=5432
            )
            self.connection.autocommit = True
            self.cur = self.connection.cursor(
                cursor_factory=psycopg2.extras.RealDictCursor)

            print('Connected to the database successfully')
            self.create_tables()

        except(Exception, psycopg2.DatabaseError) as error:
            print(error)

    def create_tables(self):
        """function  that creates tables in the database"""
        user_table = """CREATE TABLE IF NOT EXISTS users(
            user_id serial PRIMARY KEY,
            username VARCHAR(100) UNIQUE,
            email VARCHAR(100) UNIQUE,
            password VARCHAR(100) ,
            firstname VARCHAR(100),
            lastname VARCHAR(100),
            othername VARCHAR(100),
            phonenumber VARCHAR(15), 
            created_at VARCHAR(100),
            admin BOOLEAN DEFAULT False)  
            """

        incidents_table = """
            CREATE TABLE IF NOT EXISTS incidents(
            incident_id serial PRIMARY KEY,
            type VARCHAR (100),
            name VARCHAR(100),
            description VARCHAR(100),
            location VARCHAR(100),
            status VARCHAR(100) DEFAULT'draft',
            images VARCHAR(100),
            comment VARCHAR(100),
            created_at VARCHAR(100),
            user_id INT,
            FOREIGN KEY(user_id) REFERENCES users(user_id) ON DELETE CASCADE ON UPDATE CASCADE 
            )
            """

        self.cur.execute(user_table)
        self.cur.execute(incidents_table)
        print("tables created successfully")

    def drop_tables(self):
        """function that drops the tables"""

        self.cur.execute("drop table incidents")
        self.cur.execute("drop table users")
        return print('tables dropped successfully')

    def add_incident(self,incident_type, name, description, location, images, comment, created_by):
        created_at = datetime.now()
        sql = """INSERT INTO incidents(type,name, \
                 description,location,\
                images, comment,\
                created_at,user_id)\
                VALUES('{}','{}','{}','{}','{}','{}','{}','{}') RETURNING incident_id"""\
              .format(incident_type, name, description, location, images, comment, created_at,created_by)
        self.cur.execute(sql)
        incident = self.cur.fetchone()
        return incident

    def get_all_incident_records(self,current_user, incident_type):
        """function that fetches all incidents by type"""
        sql = """ SELECT * FROM incidents WHERE type='{}' AND user_id ='{}' ORDER BY created_at DESC """.format(
            incident_type, current_user)
        self.cur.execute(sql)
        incidents = self.cur.fetchall()
        return incidents

    def get_one_incident(self,current_user, incident_type, incident_id):
        """function that fetches one redflag"""
        sql = "SELECT * FROM incidents WHERE type='{}' AND incident_id='{}' AND user_id ='{}' ".format(
            incident_type, incident_id, current_user)
        self.cur.execute(sql)
        incidents = self.cur.fetchone()
        return incidents

    def delete_one_incident(self, current_user, incident_type, incident_id, ):
        """ function that deletes a redflag record"""
        delete_query = "DELETE FROM incidents WHERE type='{}' AND incident_id = '{}' AND user_id ='{}'".format(
            incident_type, incident_id, current_user)
        deleted_interv = incident_id
        self.cur.execute(delete_query)
        return deleted_interv

    def update_location(self, current_user, location, incident_type, incident_id):
        """function that updates the location"""
        sql = "UPDATE incidents SET location='{}'".format(
            location) + " WHERE type='{}' AND incident_id='{}' AND user_id ='{}'".format(incident_type, incident_id, current_user)
        self.cur.execute(sql)
        loc_id = incident_id
        return loc_id

    def update_comment(self, current_user, comment, incident_type, incident_id):
        """function that updates the comment"""
        sql = "UPDATE incidents SET comment='{}'".format(
            comment) + " WHERE type ='{}' AND incident_id='{}' AND user_id ='{}'".format(incident_type, incident_id, current_user)
        self.cur.execute(sql)
        comm_id = incident_id
        return comm_id

    # def admin_update_status(self, status, incident_type, incident_id):
    #     """function that enables the admin to update the incident status"""
    #     sql = "UPDATE incidents SET status='{}'".format(
    #         status) + " WHERE type='{}' AND incident_id='{}'".format(incident_type, incident_id)
    #     self.cur.execute(sql)
    #     stat_id = incident_id
    #     return stat_id
    
    def admin_update_status(self, status, incident_id):
        """function that enables the admin to update the incident status"""
        sql = "UPDATE incidents SET status='{}'".format(
            status) + " WHERE incident_id='{}'".format(incident_id)
        self.cur.execute(sql)
        stat_id = incident_id
        return stat_id


    def register_users(self, username, email, password, firstname, lastname, othernames, phonenumber):
        """function that registers users """
        created_at = datetime.now()
        sql = "INSERT INTO users(\
                username, email, password, firstname,\
                lastname, othername, phonenumber,created_at)"\
              " VALUES('{}','{}','{}','{}','{}','{}','{}','{}') RETURNING user_id "\
              .format(username, email, password, firstname,
                      lastname, othernames, phonenumber,created_at)
        self.cur.execute(sql)
        user = self.cur.fetchone()
        return user

    def check_email_exists(self, email):
        """function that checks and validates unique email in db"""
        sql_email = "SELECT* FROM users WHERE email='{}'".format(
            email)
        self.cur.execute(sql_email)
        row = self.cur.fetchone()
        return row

    def check_username_exists(self, username):
        """function that checks and validates unique username in db"""
        sql_username = "SELECT* FROM users WHERE username='{}'".format(
            username)
        self.cur.execute(sql_username)
        row = self.cur.fetchone()
        return row

    def check_login_user(self, username, password):
        """login user"""
        sql = "SELECT * FROM users WHERE username='{}' AND password='{}'".format(username,password)
        self.cur.execute(sql)
        users = self.cur.fetchone()
        return users
        

    def get_current_user(self, user_id):
        sql = "SELECT * FROM users WHERE username='{}'".format(user_id)
        self.cur.execute(sql)
        user = self.cur.fetchone()
        if user:
            return user
        return False

    def get_user(self, username):
        query = "SELECT * FROM users WHERE username='{}'".format(username)
        self.cur.execute(query)
        user = self.cur.fetchone()
        if user:
            return user
        return False

    def get_all_inc_records(self):
        """function that fetches all incidents for admin"""
        sql = """ SELECT * FROM incidents ORDER BY created_at DESC """
        self.cur.execute(sql)
        incidents = self.cur.fetchall()
        return incidents
    
    def get_users_db(self):
        sql = "SELECT * FROM users ORDER BY created_at DESC"
        self.cur.execute(sql)
        user = self.cur.fetchall()
        if user:
            return user
        return False

    def admin_change_user_role(self, user_role, user_id):
        sql = "UPDATE users SET admin = '{}'".format(user_role) + " WHERE user_id ='{}'".format(user_id)
        self.cur.execute(sql)
        admin_id = user_id
        return admin_id
