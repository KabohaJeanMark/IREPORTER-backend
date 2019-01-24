import psycopg2
from psycopg2 import extras
import os

class DatabaseConnect:
    """class that establishes database connection, creates various tables and drops the tables """

    def __init__(self):

        if os.getenv('DB_NAME') == "testdb":
            self.dbname = "test"
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

        intervention_table = """
            CREATE TABLE IF NOT EXISTS interventions(
            intervention_id serial PRIMARY KEY NOT NULL,
            location VARCHAR(100) NOT NULL,
            status VARCHAR(100) DEFAULT'draft',
            images VARCHAR(100) NOT NULL,
            videos VARCHAR(100) NOT NULL,
            comment VARCHAR(100) NOT NULL,
            created_at VARCHAR(100) NOT NULL,
            user_id INT NOT NULL,
            FOREIGN KEY(user_id) REFERENCES users(user_id) ON DELETE CASCADE ON UPDATE CASCADE 
            )
            """
        redflag_table = """
            CREATE TABLE IF NOT EXISTS redflags(
            redflag_id serial PRIMARY KEY NOT NULL,
            location VARCHAR(100) NOT NULL,
            status VARCHAR(100) DEFAULT'draft',
            images VARCHAR(100) NOT NULL,
            videos VARCHAR(100) NOT NULL,
            comment VARCHAR(100) NOT NULL,
            created_at VARCHAR(100) NOT NULL,
            user_id INT NOT NULL,
            FOREIGN KEY(user_id) REFERENCES users(user_id) ON DELETE CASCADE ON UPDATE CASCADE 
            )
            """

        self.cur.execute(user_table)
        self.cur.execute(intervention_table)
        self.cur.execute(redflag_table)
        print("tables created successfully")

    def drop_tables(self):
        """function that drops the tables"""
        
        self.cur.execute("delete from redflags")
        self.cur.execute("delete from interventions")
        self.cur.execute("delete from users")
        return print('tables dropped successfully')

