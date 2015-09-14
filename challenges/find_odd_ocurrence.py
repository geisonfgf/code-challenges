"""
Given an array of positive integers. All numbers occur even number of times
except one number which occurs odd number of times. Find the number in O(n)
time & constant space.

Input = [1, 2, 3, 2, 3, 1, 3]
Expected result = 3
"""

def find_odd_ocurrence(arr):
    result = 0
    for i in xrange(len(arr)):     
        result = result ^ arr[i]
    return result

if __name__ == '__main__':
    print "Input [1, 2, 3, 2, 3, 1, 3]"
    print "Expected result: 3"
    print "Result: ", find_odd_ocurrence([1, 2, 3, 2, 3, 1, 3])

    print "Input [2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2]"
    print "Expected result: 5"
    print "Result: ", find_odd_ocurrence([2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2])
