import unittest
from flatten import flatten


class FlattenTest(unittest.TestCase):

    def test_array_with_wrong_values(self):
        self.assertRaises(ValueError, lambda: flatten([1, "2"]))
        self.assertRaises(ValueError, lambda: flatten(["2"]))
        self.assertRaises(ValueError, lambda: flatten([long(2)]))
        self.assertRaises(ValueError, lambda: flatten([1, "2", []]))

    def test_array_with_nested_empty_arrays(self):
        self.assertEqual([], flatten([[[[[[]]]]],[[], []]]))

    def test_array_with_nested_empty_arrays_and_correct_values(self):
        self.assertEqual([1, 2, 3, 4, 5, 6],
                         flatten([[[[[[1]]]]],[2, [], [3], [4, 5, 6]]]))
        self.assertEqual([1, 4, 3, 2, 5, 6],
                         flatten([[[[[[1]]]]],[4, [], [3], [2, 5, 6]]]))

    def test_happy_path(self):
        self.assertEqual(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            flatten([[1, 2, 3],[[4, [[5]]], [6, 7]], 8, [[[9], [10]]]]))
        self.assertEqual(
            [1, -2, 3, -4, 5, -6, 7, -8, 9, -10],
            flatten([[1, -2, 3],[[-4, [[5]]], [-6, 7]], -8, [[[9], [-10]]]]))


if __name__ == "__main__":
    unittest.main()