from multiprocessing.sharedctypes import Value
import unittest
import principal

class TestPrincipal(unittest.TestCase):

    def test_convertToRoman(self):
        self.assertEqual(principal.convertToRoman(5), "V")
    def test_convertToRoman2(self):
        self.assertEqual(principal.convertToRoman(333), "CCCXXXIII")
    def test_convertToRoman3(self):
        self.assertEqual(principal.convertToRoman(444), "CDXLIV")
    def test_convertToRoman4(self):
        self.assertEqual(principal.convertToRoman(45000), "XLV-")
    def test_convertToRoman5(self):
        self.assertEqual(principal.convertToRoman(50000), "L-")

if __name__ == "__main__":
    unittest.main()