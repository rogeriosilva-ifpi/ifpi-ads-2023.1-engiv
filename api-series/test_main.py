import unittest


def test_hello():
    assert 1 == 1


class MainTest(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(1, 1)
