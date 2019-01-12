def find_missing_element_using_sum(arr):
    total_count = len(arr)
    expected_sum = (total_count+1) * (total_count + 2) / 2
    sum_of_arr = sum(arr)
    return expected_sum - sum_of_arr

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 6, 7, 9, 8, 10]
    print("Expected result using sum formula:", 5)
    print("Missing element is:", find_missing_element_using_sum(arr))
