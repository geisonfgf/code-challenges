def flatten(array):
    """
    This function takes an array of arbitrarily nested arrays of integers
    and flattens it into a 1 dimensional array containing the same integers.
    
    It raises a ValueError exception if array and its nested arrays contains
    values different of type integer.
    """
    flattened_array = []

    for element in array:
        if type(element) is int:
            flattened_array.append(element)
        elif type(element) is list:
            flattened_array += flatten(element)
        else:
            raise ValueError("The array value is not of type integer.")

    return flattened_array


if __name__ == '__main__':
    array = [[1, 2, 3],[[4, [[5]]], [6, 7]], 8, [[[9], [10]]]]
    print "Array before flatten: ", [[1, 2, 3],[[4, [[5]]], [6, 7]], 8, [[[9], [10]]]]
    print "Array after flatten: ", flatten(array)