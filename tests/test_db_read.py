import unittest
from pymongo import MongoClient

class TestDatabaseRead(unittest.TestCase):
    def setUp(self):
        # Set up the database connection
        self.client = MongoClient('mongodb://localhost:27017/')  # Replace with your connection string
        self.db = self.client['test_database']  # Replace with your database name

    def test_mongodb_connection(self):
        # Test MongoDB ping
        try:
            self.db.command("ping")
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"MongoDB connection failed: {str(e)}")
