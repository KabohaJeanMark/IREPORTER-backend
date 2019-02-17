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
        elif os.getenv('DB_NAME') == "proddb":
            self.dbname = "ddo76jqcvdgpp6"
            self.user = "iahxwhjlgkymau"
            self.password = "86ca7ea32a682d6e997410bd6ce1093093a51f2b3ba4ba9c9bb5a2efb0598e41"
            self.host = "ec2-54-221-253-228.compute-1.amazonaws.com"
        else:
            self.dbname = "ireporter"
            self.user = "postgres"
            self.password = ""
            self.host = "127.0.0.1"
        try:
            self.connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                host= self.host,
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
            user_id serial PRIMARY KEY NOT NULL ,
            username VARCHAR(100) UNIQUE NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            password VARCHAR(100) NOT NULL,
            firstname VARCHAR(100)  NOT NULL,
            lastname VARCHAR(100)  NOT NULL,
            othername VARCHAR(100)  NOT NULL,
            phonenumber VARCHAR(15)  NOT NULL, 
            created_at VARCHAR(100) NOT NULL,
            admin BOOLEAN DEFAULT FALSE) 
            """

        incidents_table = """
            CREATE TABLE IF NOT EXISTS incidents(
            incident_id serial PRIMARY KEY,
            type VARCHAR (20),
            name VARCHAR(20),
            description VARCHAR(100),
            latitude VARCHAR(10),
            longitude VARCHAR(10),
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

    def add_incident(self, incident_type, name, description,latitude, longitude, images, comment, created_by):
        created_at = datetime.now()
        sql = """INSERT INTO incidents(type,name, \
                 description,latitude,\
                longitude,images, comment,\
                created_at, user_id)\
                VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}') RETURNING incident_id"""\
              .format(incident_type, name, description,latitude, longitude, images, comment, created_at, created_by)
        self.cur.execute(sql)
        incident = self.cur.fetchone()
        return incident

    def get_all_incident_records(self, incident_type):
        """function that fetches all incidents by type"""
        sql = """ SELECT * FROM incidents WHERE type='{}' ORDER BY created_at DESC """.format(incident_type)
        self.cur.execute(sql)
        incidents = self.cur.fetchall()
        return incidents

    def get_one_incident(self, incident_type, incident_id):
        """function that fetches one redflag"""
        sql = "SELECT * FROM incidents WHERE type='{}' AND incident_id='{}'".format(
            incident_type,incident_id)+"ORDER BY created_at DESC"
        self.cur.execute(sql)
        incidents = self.cur.fetchone()
        return incidents