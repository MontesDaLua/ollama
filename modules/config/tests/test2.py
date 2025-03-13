"""
Dummy test2
"""
import unittest

class TestConfig1(unittest.TestCase):
    """
    Config modules test suit 2
    """

    def test1(self):
        """
        test1 docString
        """
        self.assertEqual(1,1)

    def test2(self):
        """
        test2 docString
        """
        self.assertNotEqual(1,2)

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

    def test5(self):
        """
        test5 docString
        """
        a = 3
        b = 3
        self.assertIs(a, b)

    def test6(self):
        """
        test6 docString
        """
        x = None
        self.assertIsNone(x)

    def test7(self):
        """
        test7 docString
        """
        my_list = [1,2,3]
        x = 2
        self.assertIn(x, my_list)
