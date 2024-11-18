import unittest
from pymongo import MongoClient

class TestDatabaseWrite(unittest.TestCase):
    def setUp(self):
        # Set up the database connection
        self.client = MongoClient('mongodb://localhost:27017/')  # Replace with your connection string
        self.db = self.client['test_database']  # Replace with your database name
        self.collection = self.db['test_collection']  # Replace with your collection name

    def test_mongodb_write(self):
        # Insert a test document
        data = {"name": "Test User", "email": "test@example.com"}
        result = self.collection.insert_one(data)

        # Verify the document was inserted
        inserted_doc = self.collection.find_one({"_id": result.inserted_id})
        self.assertIsNotNone(inserted_doc)
        self.assertEqual(inserted_doc['name'], "Test User")
        self.assertEqual(inserted_doc['email'], "test@example.com")
