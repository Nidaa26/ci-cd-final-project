"""Unit tests for the Flask microservice."""
import unittest
from app import app


class TestApp(unittest.TestCase):
    """Test cases for the application routes."""

    def setUp(self):
        self.client = app.test_client()

    def test_index(self):
        """It should return 200 and a welcome message on the root route"""
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b"Welcome", resp.data)

    def test_health(self):
        """It should return 200 and status OK on the health route"""
        resp = self.client.get("/health")
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b"OK", resp.data)


if __name__ == "__main__":
    unittest.main()
