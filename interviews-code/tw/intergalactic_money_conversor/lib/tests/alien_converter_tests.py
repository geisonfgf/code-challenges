import unittest, os.path as path, sys
from inspect import getsourcefile
current_dir = path.dirname(path.abspath(getsourcefile(lambda:0)))
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)])
from alien_converter import AlienNumeral, AlienMaterial, AlienConverter
from alien_converter import InvalidAlienNumeralError, InvalidAlienMaterialError
sys.path.pop(0)


class TestAlienNumeral(unittest.TestCase):
    
    def setUp(self):
        self.alien_numeral = AlienNumeral()        

    def test_add_alien_numeral(self):
        self.alien_numeral["glob"] = {"roman": "I", "arabic": 1}
        self.assertEqual(self.alien_numeral["glob"], {"roman": "I", "arabic": 1})

    def test_add_alien_numeral_erros(self):
        with self.assertRaises(InvalidAlienNumeralError):
            self.alien_numeral['glob'] = "IIII"


class TestAlienMaterial(unittest.TestCase):
    
    def setUp(self):
        self.alien_material = AlienMaterial()        

    def test_add_alien_material(self):
        self.alien_material["Gold"] = 112.5
        self.assertEqual(self.alien_material["Gold"], 112.5)

    def test_add_alien_material_erros(self):
        with self.assertRaises(InvalidAlienMaterialError):
            self.alien_material['material'] = ""
        with self.assertRaises(InvalidAlienMaterialError):
            self.alien_material['Gold'] = ""


class TestAlienConverter(unittest.TestCase):
    
    def setUp(self):
        self.alien_converter = AlienConverter()
        self.alien_converter.alien_numerals["glob"] = {"roman": "I", "arabic": 1}
        self.alien_converter.alien_numerals["prok"] = {"roman": "V", "arabic": 5}
        self.alien_converter.alien_numerals["pish"] = {"roman": "X", "arabic": 10}
        self.alien_converter.alien_numerals["tegj"] = {"roman": "L", "arabic": 50}

    def test_sum_alien_numerals(self):
        self.assertEqual(self.alien_converter.sum_alien_numerals(["prok", "glob", "glob", "glob"]), 8)
        self.assertEqual(self.alien_converter.sum_alien_numerals(["pish", "tegj", "glob", "prok"]), 44)

    def test_sum_alien_numerals_errors(self):
        self.assertRaises(InvalidAlienNumeralError, self.alien_converter.sum_alien_numerals, [])


if __name__ == '__main__':
    unittest.main()
