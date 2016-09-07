"""Converter from Roman to numerals"""

import re

#Define exceptions
class RomanError(Exception): pass
class InvalidRomanNumeralError(RomanError): pass

#Define digit mapping
roman_numerals = (('M',  1000),
                  ('CM', 900),
                  ('D',  500),
                  ('CD', 400),
                  ('C',  100),
                  ('XC', 90),
                  ('L',  50),
                  ('XL', 40),
                  ('X',  10),
                  ('IX', 9),
                  ('V',  5),
                  ('IV', 4),
                  ('I',  1))

#Define pattern to detect valid Roman numerals
roman_numeral_pattern = re.compile("""
    ^                   # beginning of string
    M{0,4}              # thousands - 0 to 4 M's
    (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 C's),
                        #            or 500-800 (D, followed by 0 to 3 C's)
    (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 X's),
                        #        or 50-80 (L, followed by 0 to 3 X's)
    (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 I's),
                        #        or 5-8 (V, followed by 0 to 3 I's)
    $                   # end of string
    """, re.VERBOSE)

def roman_to_numeral(roman_numeral):
    """
    Convert Roman numeral to integer
    
    :roman_numeral: a roman numeral. E.g: III, IV, V
    """
    if not roman_numeral:
        raise InvalidRomanNumeralError('Input can not be blank')
    if not roman_numeral_pattern.search(roman_numeral):
        raise InvalidRomanNumeralError(
            'Invalid Roman numeral: %s' % roman_numeral)

    result, index = 0, 0

    for numeral, integer in roman_numerals:
        while roman_numeral[index:index+len(numeral)] == numeral:
            result += integer
            index += len(numeral)
    return result