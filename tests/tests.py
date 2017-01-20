import unittest
from core.scraping import Scraping
from core.app import *
import json

class WordCounterTestCase(unittest.TestCase):

    def setUp(self):
        self.tester = app.test_client(self)

    def tearDown(self):
        pass

    def test_empty_parameters(self):
        response = self.tester.get("/word_counter", content_type="html/text")
        json_data = json.loads(response.get_data().decode("utf-8"))
        self.assertEqual(json_data, {"error": "URL cannot be blank!"})
        self.assertEqual(response.status_code, 200)

    def test_url_parameter_empty(self):
        response = self.tester.get("/word_counter?url=&word=python", content_type="html/text")
        json_data = json.loads(response.get_data().decode("utf-8"))
        self.assertEqual(json_data, {"error": "URL cannot be blank!"})
        self.assertEqual(response.status_code, 200)

    def test_word_parameter_empty(self):
        response = self.tester.get("/word_counter?url=https://docs.python.org/3&word=", content_type="html/text")
        json_data = json.loads(response.get_data().decode("utf-8"))
        self.assertEqual(json_data, {"error": "Word cannot be blank!"})
        self.assertEqual(response.status_code, 200)

    def test_url_without_protocol(self):
        response = self.tester.get("/word_counter?url=docs.python.org/3&word=python", content_type="html/text")
        json_data = json.loads(response.get_data().decode("utf-8"))
        self.assertEqual(json_data, {"error": "URL is not valid!"})
        self.assertEqual(response.status_code, 200)

    def test_correct_call(self):
        response = self.tester.get("/word_counter?url=https://docs.python.org/3&word=python", content_type="html/text")
        json_data = json.loads(response.get_data().decode("utf-8"))
        self.assertEqual(json_data, {"python": 18})