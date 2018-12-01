import unittest
from Basic.unittest_lesson import myClass


class Test_myClass2(unittest.TestCase):

    def setUp(self):
        self.f = myClass.Father()

    def test_add(self):
        #f = myClass.Father()
        result1 = self.f.add(100,50)
        self.assertEqual(result1,50)

    def test_minus(self):
        #f = myClass.Father()
        result2 = self.f.minus(100,40)
        self.assertEqual(result2,60)
