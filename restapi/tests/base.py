import unittest
from restapi import app
from restapi.models.database import DatabaseConnect


class TestDb(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.db = DatabaseConnect()
        self.db.create_tables()

    def tearDown(self):
        self.db.drop_tables()

if __name__ == '__main__':
    unittest.main()