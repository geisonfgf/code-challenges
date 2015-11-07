import unittest
from itertools import islice
from read_file import read_file_generator, convert_string_json_to_python_dict
from calculate_distance import calculate_distance
from get_customers_in_a_100km_range import get_all_customers_from_file, get_customers_in_a_range_of_100km


class GetCustomerInA100KmRangeTest(unittest.TestCase):

    def test_read_file_generator_with_wrong_path(self):
        self.assertRaises(IOError, lambda: list(read_file_generator("wrong_path")))

    def test_read_file_generator_right_path(self):
        self.assertEqual(
            list(islice(read_file_generator("customers.json"), 1)),
            ['{"latitude": "52.986375", "user_id": 12, "name": "Christina McArdle", "longitude": "-6.043701"}\n'])

    def test_convert_string_json_to_python_dict_with_invalid_json(self):
        self.assertRaises(ValueError, lambda: convert_string_json_to_python_dict("{'id': 1, 'name': 'test'}"))

    def test_convert_string_json_to_python_dict_with_valid_json(self):
        self.assertEqual({u'id': 1, u'name': u'test'}, convert_string_json_to_python_dict('{"id": 1, "name": "test"}'))

    def test_calculate_distance_with_wrong_parameters(self):
        self.assertRaises(ValueError, lambda: calculate_distance("wrong_value", 1, 2, 3))

    def test_calculate_distance_with_correct_parameters(self):
        self.assertEqual(41.68, calculate_distance(53.3381985, -6.2592576, 52.986375, -6.043701))
        self.assertEqual(313.1, calculate_distance(53.3381985, -6.2592576, 51.92893, -10.27699))
        self.assertEqual(324.22, calculate_distance(53.3381985, -6.2592576, 51.8856167, -10.4240951))

    def test_get_all_customers_from_file_with_wrong_path_file(self):
        self.assertRaises(IOError, lambda: list(get_all_customers_from_file("wrong_path")))

    def test_get_all_customers_from_file(self):
        self.assertEqual(
            list(islice(get_all_customers_from_file("customers.json"), 1)),
            [{u'latitude': u'52.986375', u'user_id': 12, u'name': u'Christina McArdle', u'longitude': u'-6.043701'}])

    def test_get_customers_in_a_range_of_100km_with_wrong_values(self):
        customers = [{"test": "test"}]
        self.assertRaises(ValueError, lambda: get_customers_in_a_range_of_100km(customers))

    def test_get_customers_in_a_range_of_100km(self):
        customers = get_all_customers_from_file("customers.json")
        customers_in_100Km_range = get_customers_in_a_range_of_100km(customers)
        self.assertEqual(32, len(customers))
        self.assertEqual(16, len(customers_in_100Km_range))
        

if __name__ == '__main__':
    unittest.main()
