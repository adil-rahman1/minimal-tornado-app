import unittest
from tornado.testing import AsyncHTTPTestCase
from app import make_app
import re

class TestMainHandler(AsyncHTTPTestCase):
    def get_app(self):
        return make_app()

    def test_background_colour_changer(self):
        response = self.fetch('/')
        self.assertIn(b"Change my background color by clicking the button below", response.body)

    def test_nav_in_index(self):
        response = self.fetch('/')
        self.assertIn(b"<nav>", response.body)

    def test_links_in_index(self):
        response = self.fetch('/')
        content = response.body.decode(encoding='utf-8')
        self.assertEqual(content.count("<li>"), 4)

if __name__ == "__main__":
    unittest.main()