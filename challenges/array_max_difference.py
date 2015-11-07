def max_diff(arr):
    return max(arr) - min(arr)

if __name__ == '__main__':
    arr = [1, 2, 6, 80, 100]
    print "Expected result:", 99
    print "Maximum difference is:", max_diff(arr)
