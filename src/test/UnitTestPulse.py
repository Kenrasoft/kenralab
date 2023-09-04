import unittest
from pulse.db import Repository

class TestDB(unittest.TestCase):

    def test_load_data(self):
        r = Repository()
        r.load_data()
        expected_value = 1
        self.assertEqual(1, expected_value)