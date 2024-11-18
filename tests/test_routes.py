import unittest
from app import app  # Import your Flask app

class TestRoutes(unittest.TestCase):
    def setUp(self):
        # Set up the Flask test client
        self.app = app.test_client()
        self.app.testing = True

    def test_home_post(self):
        # Simulate a POST request to a GET-only route
        response = self.app.post('/home')  # Replace '/home' with your actual route
        self.assertEqual(response.status_code, 405)  # 405 Method Not Allowed
