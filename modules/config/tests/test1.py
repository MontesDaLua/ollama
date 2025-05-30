"""
Dummy test1
"""
import unittest

class TestConfig1(unittest.TestCase):
    """
    Config modules test suit 1
    """

    def test1(self):
        """
        test1 docString
        """
        self.assertEqual(2,2)

    def test2(self):
        """
        test2 docString
        """
        self.assertNotEqual(4,2)

    def test3(self):
        """
        test3 docString
        """
        v = True
        self.assertTrue(v)

    def test4(self):
        """
        test4 docString
        """
        v = False
        self.assertFalse(v)
