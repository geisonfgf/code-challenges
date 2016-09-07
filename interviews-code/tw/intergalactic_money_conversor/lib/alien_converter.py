"""Converter from Alien to numerals"""

from roman_converter import roman_to_numeral, InvalidRomanNumeralError


#Define exceptions
class AlienError(Exception): pass
class InvalidAlienNumeralError(AlienError): pass
class InvalidAlienMaterialError(AlienError): pass


class AlienNumeral(dict):
    
    def __init__(self, *args, **kwargs):
        """Construct a new 'AlienNumeral' object."""
        dict.__init__(self,*args,**kwargs)

    def __getitem__(self, key):
        """Return the alien numerals"""
        val = dict.__getitem__(self, key)
        return val

    def __setitem__(self, key, val):
        """
        Add a Alien numeral and its values
        
        :key: a string containing the Alien Numeral name
        :val: a Dict containing the Alien roman and
        arabic values. E.g: {'roman': "V", 'arabic': 5}
        """
        if not (isinstance(val, dict)):
            raise InvalidAlienNumeralError(
                'Invalid Alien numeral: {"%s": %s}' % (key, val))
        dict.__setitem__(self, key, val)

    def __repr__(self):
        dictrepr = dict.__repr__(self)
        return '%s(%s)' % (type(self).__name__, dictrepr)


class AlienMaterial(dict):
    
    def __init__(self, *args, **kwargs):
        """Construct a new 'AlienMaterial' object."""
        dict.__init__(self,*args,**kwargs)

    def __getitem__(self, key):
        """Return the alien material"""
        val = dict.__getitem__(self, key)
        return val

    def __setitem__(self, key, val):
        """
        Add a Alien material and its value
        
        :key: string material name. E.g: Silver, Gold or Iron
        :val: int value
        """
        if not (key in ["Silver", "Gold", "Iron"] and isinstance(val, float)):
            raise InvalidAlienMaterialError(
                'Invalid Alien material: {"%s": %s}' % (key, val))
        dict.__setitem__(self, key, val)

    def __repr__(self):
        dictrepr = dict.__repr__(self)
        return '%s(%s)' % (type(self).__name__, dictrepr)


class AlienConverter:

    def __init__(self):
        """Construct a new 'AlienConverter' object."""
        self.alien_numerals = AlienNumeral()
        self.materials = AlienMaterial()

    def sum_alien_numerals(self, alien_numerals):
        """
        Return the sum of alien numerals
        
        :alien_numerals: a list containing alien numerals
        E.g. ["glob", "glob"]
        """
        try:
            roman_numeral = reduce(
                lambda first_value, second_value: first_value + second_value,
                [self.alien_numerals[alien_numeral]['roman']
                for alien_numeral in alien_numerals])
            number = roman_to_numeral(roman_numeral)
        except Exception:
            raise InvalidAlienNumeralError(
                'Invalid Alien numeral: "%s"' % alien_numerals)
        return number
