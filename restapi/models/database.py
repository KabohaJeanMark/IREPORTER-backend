import psycopg2
from psycopg2 import extras

class DatabaseConnect:
    """class that establishes database connection, creates various tables and drops the tables """

    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                dbname='ireporter', user='postgres', host='localhost', password='', port=5432
            )
            self.connection.autocommit = True
            self.cur = self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

            print('Connected to the database successfully.')
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
    def create_tables(self):
        """function  that creates tables in the database"""
        queries = (
            """CREATE TABLE IF NOT EXISTS users(
            user_id serial PRIMARY KEY NOT NULL ,
            username UNIQUE VARCHAR(100)  NOT NULL,
            firstname VARCHAR(100)  NOT NULL,
            lastname VARCHAR(100)  NOT NULL,
            othername VARCHAR(100)  NOT NULL,
            email UNIQUE VARCHAR(100)NOT NULL,
            password VARCHAR(100) NOT NULL,
            create_at VARCHAR(100) NOT NULL,
            admin BOOLEAN DEFAULT FALSE 
            )""",
            """
            CREATE TABLE IF NOT EXISTS interventions(
            intervention_id serial PRIMARY KEY NOT NULL,
            receivers VARCHAR(100) NOT NULL,
            description VARCHAR(100) NOT NULL,
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
        )
     
    
        for tables in queries:
            self.cur.execute(tables)
        print("tables created successfully")

    def drop_tables(self):
        """function that drops the tables"""
        query = "TRUNCATE TABLE users, parcel_orders RESTART IDENTITY "
        self.cur.execute(query)
        return print('tables dropped successfully')

    

    