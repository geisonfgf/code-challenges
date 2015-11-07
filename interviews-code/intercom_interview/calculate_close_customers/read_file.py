import json


def read_file_generator(file_path):
    """
    This function takes the file path, read the file and return a generator
    of each line

    It raise a IOError in case the file_path parameter are wrong
    """
    with open(file_path, 'r') as f:
        for line in f:
            yield line

def convert_string_json_to_python_dict(string_json):
    """
    This function takes a string json and return a python dict

    It raise a ValueError Exception in case the string_json parameter are not
    a valid json format
    """
    return json.loads(string_json)
