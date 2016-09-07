import unittest, os.path as path, sys
from inspect import getsourcefile
current_dir = path.dirname(path.abspath(getsourcefile(lambda:0)))
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)])
from roman_converter import roman_to_numeral, InvalidRomanNumeralError
sys.path.pop(0)

class TestRomanConverter(unittest.TestCase):

    def test_roman_to_numeral(self):
        self.assertEqual(roman_to_numeral('I'), 1)
        self.assertEqual(roman_to_numeral('II'), 2)
        self.assertEqual(roman_to_numeral('III'), 3)
        self.assertEqual(roman_to_numeral('IV'), 4)
        self.assertEqual(roman_to_numeral('V'), 5)
        self.assertEqual(roman_to_numeral('VI'), 6)
        self.assertEqual(roman_to_numeral('VII'), 7)
        self.assertEqual(roman_to_numeral('VIII'), 8)
        self.assertEqual(roman_to_numeral('IX'), 9)
        self.assertEqual(roman_to_numeral('X'), 10)
        self.assertEqual(roman_to_numeral('XX'), 20)
        self.assertEqual(roman_to_numeral('XXX'), 30)
        self.assertEqual(roman_to_numeral('XXXVIII'), 38)
        self.assertEqual(roman_to_numeral('XL'), 40)
        self.assertEqual(roman_to_numeral('L'), 50)
        self.assertEqual(roman_to_numeral('LX'), 60)
        self.assertEqual(roman_to_numeral('XCIX'), 99)
        self.assertEqual(roman_to_numeral('C'), 100)
        self.assertEqual(roman_to_numeral('MMXIII'), 2013)
        self.assertEqual(roman_to_numeral('MCMLXXXIII'), 1983)
        self.assertEqual(roman_to_numeral('MMMDCCCLXXXVIII'), 3888)

    def test_roman_to_numeral_errors(self):
        self.assertRaises(InvalidRomanNumeralError, roman_to_numeral, '')
        self.assertRaises(InvalidRomanNumeralError, roman_to_numeral, 'Q12')
        self.assertRaises(InvalidRomanNumeralError, roman_to_numeral, 'IVI')
        self.assertRaises(InvalidRomanNumeralError, roman_to_numeral, 'IIII')        
        self.assertRaises(
            InvalidRomanNumeralError, roman_to_numeral, 'MCCMLXXXIII')

if __name__ == '__main__':
    unittest.main()
