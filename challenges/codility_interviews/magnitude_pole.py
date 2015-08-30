"""
Magnitude Pole: An element in an array whose left hand side elements are
lesser than or equal to it and whose right hand side element are greater
than or equal to it.

Input:
    [3, 1, 4, 5, 9, 7, 6, 11]

Output:
    4

Time complexity O(N)
Space complexity O(N)
"""

from sys import maxint

def solution(A):
    length = len(A)
    aux_maxes = [0] * length
    aux_mins = [0] * length

    max_value, aux_maxes[0] = -maxint, -maxint
    min_value, aux_mins[length - 1] = maxint, maxint

    for i in xrange(length-1, -1, -1):
        if A[i] < min_value:
            min_value = A[i]
        aux_mins[i] = min_value

    for i in xrange(length):
        if A[i] > max_value:
            max_value = A[i]
        aux_maxes[i] = max_value

    for i in xrange(length):
        if A[i] >= aux_maxes[i] and A[i] <= aux_mins[i]:
            if i == 0:
                return -1
            return A[i]

    return -1

print "Input: [3, 1, 4, 5, 9, 7, 6, 11]"
print "Expected answer: 4"
print "My answer: ", solution([3, 1, 4, 5, 9, 7, 6, 11])

print "Input: [1, 2, 3, 4, 5, 6, 7, 8]"
print "Expected answer: -1"
print "My answer: ", solution([1, 2, 3, 4, 5, 6, 7, 8])

print "Input: [8, 7, 6, 5, 4, 3, 2, 1]"
print "Expected answer: -1"
print "My answer: ", solution([8, 7, 6, 5, 4, 3, 2, 1])

print "Input: [2, 1, 3, 5, 4, 8, 6, 7]"
print "Expected answer: 3"
print "My answer: ", solution([2, 1, 3, 5, 4, 8, 6, 7])