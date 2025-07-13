import unittest
import sys
import os

# Add parent dir of tests/ to sys.path to import app
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app  # assuming app.py is in 05_flask-jenkins-project/

class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        # ✅ Update the expected text below
        self.assertIn(b'Welcome to the Flask CI/CD Demo!', response.data)

if __name__ == '__main__':
    unittest.main()
