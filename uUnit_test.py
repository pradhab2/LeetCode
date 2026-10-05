import unittest
from ebay_indexOf_insrt_int import bsr

class TestSuite(unittest.TestCase):
    def testResultPositive(self):
        self.assertEqual(bsr([4,7,9,12,45],0,5,1),0,"The result is matching with the expected result")
    def testResultNegetive(self):
        self.assertEqual(bsr([4,7,9,12,45],0,5,56),9,"The result is matching with the expected result")

if __name__=='__main__':
    unittest.main(verbosity=2)
