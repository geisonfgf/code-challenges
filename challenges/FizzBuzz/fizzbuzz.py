'''FizzBuzz

Write a program that prints the numbers from 0 to 100 following the rules:
- multiples of three print "Fizz".
- multiples of five print "Buzz".
- multiples of both three and five print "FizzBuzz".
- other numbers print the number itself.
'''

import unittest


class FizzBuzz(object):

    def evaluate(self, number):

        assert 0 <= number <= 100, (
               'number parameter must be a number between 0-100')

        if number == 0:
            return 0

        result = ''

        if self.__number_is_divisible_by_three(number):
            result += 'Fizz'

        if self.__number_is_divisible_by_five(number):
            result += 'Buzz'

        return result if result else number

    def up_to(self, to):

        assert isinstance(to, int) and to >= 0, (
               'to parameter must be a integer >= 0')

        return [self.evaluate(number) for number in range(to)]

    def from_to(self, fr, to):

        assert ((isinstance(fr, int)) and
                (isinstance(to, int)) and
                (to >= 0 and fr < to)), (
               'fr and to parameters must be a integer >= 0 and fr < to')

        return [self.evaluate(number) for number in range(fr, to+1)]

    def __number_is_divisible_by_three(self, number):
        return number % 3 == 0

    def __number_is_divisible_by_five(self, number):
        return number % 5 == 0


def fizzbuzz(number):
    assert 0 <= number <= 100, (
           'number parameter must be a number between 0-100')
    if number == 0:
        return 0
    result = ''
    if number % 3 == 0:
        result += 'Fizz'
    if number % 5 == 0:
        result += 'Buzz'
    return result if result else number


class TestFizzBuzz(unittest.TestCase):

    def setUp(self):
        self.fizzbuzz = FizzBuzz()

    def test_fizzbuzz_of_zero(self):
        self.assertEqual(fizzbuzz(0), 0)
        self.assertEqual(self.fizzbuzz.evaluate(0), 0)

    def test_fizzbuzz_of_one(self):
        self.assertEqual(fizzbuzz(1), 1)
        self.assertEqual(self.fizzbuzz.evaluate(1), 1)

    def test_fizzbuzz_of_two(self):
        self.assertEqual(fizzbuzz(2), 2)
        self.assertEqual(self.fizzbuzz.evaluate(2), 2)

    def test_fizzbuzz_of_three(self):
        self.assertEqual(fizzbuzz(3), 'Fizz')
        self.assertEqual(self.fizzbuzz.evaluate(3), 'Fizz')

    def test_fizzbuzz_of_four(self):
        self.assertEqual(fizzbuzz(4), 4)
        self.assertEqual(self.fizzbuzz.evaluate(4), 4)

    def test_fizzbuzz_of_five(self):
        self.assertEqual(fizzbuzz(5), 'Buzz')
        self.assertEqual(self.fizzbuzz.evaluate(5), 'Buzz')

    def test_fizzbuzz_of_six(self):
        self.assertEqual(fizzbuzz(6), 'Fizz')
        self.assertEqual(self.fizzbuzz.evaluate(6), 'Fizz')

    def test_fizzbuzz_of_seven(self):
        self.assertEqual(fizzbuzz(7), 7)
        self.assertEqual(self.fizzbuzz.evaluate(7), 7)

    def test_fizzbuzz_of_ten(self):
        self.assertEqual(fizzbuzz(10), 'Buzz')
        self.assertEqual(self.fizzbuzz.evaluate(10), 'Buzz')

    def test_fizzbuzz_of_fifteen(self):
        self.assertEqual(fizzbuzz(15), 'FizzBuzz')
        self.assertEqual(self.fizzbuzz.evaluate(15), 'FizzBuzz')

    def test_fizzbuzz_of_thirty(self):
        self.assertEqual(fizzbuzz(30), 'FizzBuzz')
        self.assertEqual(self.fizzbuzz.evaluate(30), 'FizzBuzz')

    def test_fizzbuzz_of_negative_numbers(self):
        self.assertRaises(AssertionError, lambda: fizzbuzz(-1))
        self.assertRaises(AssertionError, lambda: self.fizzbuzz.evaluate(-1))

    def test_fizzbuzz_of_non_number_value(self):
        self.assertRaises(AssertionError, lambda: fizzbuzz('number'))
        self.assertRaises(AssertionError, lambda: self.fizzbuzz.evaluate('number'))

    def test_fizzbuzz_of_zero_to_hundred(self):
        self.assertEqual(self.fizzbuzz.up_to(100),
                         [0, 1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz',
                          'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz', 16, 17,
                          'Fizz', 19, 'Buzz', 'Fizz', 22, 23, 'Fizz', 'Buzz',
                          26, 'Fizz', 28, 29, 'FizzBuzz', 31, 32, 'Fizz', 34,
                          'Buzz', 'Fizz', 37, 38, 'Fizz', 'Buzz', 41, 'Fizz',
                          43, 44, 'FizzBuzz', 46, 47, 'Fizz', 49, 'Buzz',
                          'Fizz', 52, 53, 'Fizz', 'Buzz', 56, 'Fizz', 58, 59,
                          'FizzBuzz', 61, 62, 'Fizz', 64, 'Buzz', 'Fizz', 67,
                          68, 'Fizz', 'Buzz', 71, 'Fizz', 73, 74, 'FizzBuzz',
                          76, 77, 'Fizz', 79, 'Buzz', 'Fizz', 82, 83, 'Fizz',
                          'Buzz', 86, 'Fizz', 88, 89, 'FizzBuzz', 91, 92,
                          'Fizz', 94, 'Buzz', 'Fizz', 97, 98, 'Fizz'])

    def test_fizzbuzz_of_zero_to_hundred(self):
        self.assertEqual(self.fizzbuzz.from_to(25, 50),
                         ['Buzz', 26, 'Fizz', 28, 29, 'FizzBuzz', 31, 32,
                          'Fizz', 34,'Buzz', 'Fizz', 37, 38, 'Fizz', 'Buzz',
                          41, 'Fizz', 43, 44, 'FizzBuzz', 46, 47, 'Fizz', 49,
                          'Buzz'])


if __name__ == '__main__':
    unittest.main()
