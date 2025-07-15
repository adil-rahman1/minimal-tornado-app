import unittest
from tornado.testing import AsyncHTTPTestCase
from app import make_app

class TestMainHandler(AsyncHTTPTestCase):
    def get_app(self):
        return make_app()

    def test_homepage(self):
        response = self.fetch('/')
        self.assertEqual(response.code, 200)
        self.assertIn(b"Change my background color by clicking the button below", response.body)

if __name__ == "__main__":
    unittest.main()