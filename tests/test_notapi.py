import unittest
import Notapi


class TestNotapi(unittest.TestCase):
    def test_napi(self):
        self.assertIsNotNone(Notapi)
        self.assertIsNotNone(Notapi.NotionTool)
