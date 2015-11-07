def min_diff(arr):
    min_value = min(arr)
    second_min_value = arr[0] if arr[0] != min_value else arr[1]
    for i in xrange(1, len(arr)):
        if arr[i] < arr[i - 1] and arr[i] != min_value:
            second_min_value = arr[i]
    return second_min_value - min_value

if __name__ == '__main__':
    arr = [5, 8, 16, 26, 4]
    print "Expected: 1"
    print "Result: ", min_diff(arr)
