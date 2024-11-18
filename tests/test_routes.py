import unittest
from app import app

class TestRoutes(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.app = app.test_client()
        cls.app.testing = True

    def test_home_get(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)  # Expecting 200 OK for GET request

    # Other test methods...

if __name__ == '__main__':
    unittest.main()