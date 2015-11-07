from read_file import read_file_generator, convert_string_json_to_python_dict
from calculate_distance import calculate_distance


def get_all_customers_from_file(file_path):
    """
    This function takes the file path that contains a json with
    a list of customers in the following format:
    {"latitude": "52.986375", "user_id": 12, "name": "Christina McArdle", "longitude": "-6.043701"}
    {"latitude": "51.92893", "user_id": 1, "name": "Alice Cahill", "longitude": "-10.27699"}
    {"latitude": "51.8856167", "user_id": 2, "name": "Ian McArdle", "longitude": "-10.4240951"}
    
    And return a list of customers in this format:
    [{u'latitude': u'52.986375', u'user_id': 12, u'name': u'Christina McArdle', u'longitude': u'-6.043701'},
     {u'latitude': u'51.92893', u'user_id': 1, u'name': u'Alice Cahill', u'longitude': u'-10.27699'},
     {u'latitude': u'51.8856167', u'user_id': 2, u'name': u'Ian McArdle', u'longitude': u'-10.4240951'}]

    It raise a IOError in case the file_path parameter are wrong
    """
    return [convert_string_json_to_python_dict(customer)
            for customer in read_file_generator(file_path)]

def get_customers_in_a_range_of_100km(customers):
    """
    This function takes a dictionary of customers that contains a
    latitude and a longitude properties for each customer and return the
    customers in a range of 100Km of distance from Intercom office

    It raise a ValueError Exception in case a customer element of dictionary
    do not have a user_id, name, latitude or longitude keys
    """
    office_latitude = 53.3381985
    office_longitude = -6.2592576
    close_customers = []

    for customer in customers:
        if not customer.has_key("latitude") or not customer.has_key("longitude"):
            raise ValueError(
                "The customer dictionary needs to have a user_id, name, latitude and longitude keys.")
        distance_from_office = calculate_distance(office_latitude,
                                                  office_longitude,
                                                  float(customer["latitude"]),
                                                  float(customer["longitude"]))
        
        if distance_from_office <= 100.0:
            close_customers.append([customer["user_id"], customer["name"]])

    return sorted(close_customers)

def print_customers(customers):
    """
    This function takes a list of customers that contains the
    user id and the name of each user and print each element
    in this format:

    Id: 1, Name: User1
    """
    for customer in customers:
        print "Id: ", customer[0], ", Name: ", customer[1]

def main():
    customers = get_all_customers_from_file("customers.json")
    customers_in_100Km_range = get_customers_in_a_range_of_100km(customers)
    print_customers(customers_in_100Km_range)


if __name__ == '__main__':
    main()
