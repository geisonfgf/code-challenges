"""
A non-empty zero-indexed array A consisting of N integers is given.

You can perform a single swap operation in array A. This operation takes two indices I and J, such that 0 <= I <= J < N, and exchanges the values of A[I] and A[J].

The goal is to check whether array A can be sorted into non-decreasing order by performing at most one swap operation.

For example, consider array A such that:

    A[0] = 1
    A[1] = 5
    A[2] = 3
    A[3] = 3
    A[4] = 7
After exchanging the values A[1] and A[3] we obtain an array [1, 3, 3, 5, 7], which is sorted in non-decreasing order.

Write a function:

def solution(A)

that, given a non-empty zero-indexed array A consisting of N integers, returns true if the array can be sorted into non-decreasing order by performing at most one swap operation or false otherwise.

For example, given:

    A[0] = 1
    A[1] = 5
    A[2] = 3
    A[3] = 3
    A[4] = 7
the function should return true, as explained above.

On the other hand, for the following array:

    A[0] = 1
    A[1] = 3
    A[2] = 5
    A[3] = 3
    A[4] = 4
the function should return false, as there is no single swap operation that sorts the array.

For the following array:

    A[0] = 1
    A[1] = 3
    A[2] = 5
the function should return true, as the given array is already sorted.

Assume that:

N is an integer within the range [1..100];
each element of array A is an integer within the range [1..1,000,000,000].
In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.
"""

import unittest

def solution(A):
    swap = 0
    arr_sorted = sorted(A)
    if arr_sorted == A:
        return True
    while A != arr_sorted:
        for i in xrange(len(A)):
            for j in xrange(len(A)):
                if A[i] > A[j] and i < j:
                    index = j
                    while A[index] == A[j] and index < j:
                    	index += 1
                    A[j], A[i] = A[i], A[j]
                    swap += 1
                    if swap > 1 and A != arr_sorted:
                        return False
    return True

class TestIfArrayIsSortedWithAtMostOneSwap(unittest.TestCase):

    def runTest(self):
        A = [1, 5, 3, 3, 7]
        A2 = [1, 5, 3, 3, 3, 7]
        B = [1, 3, 5, 3, 7]
        C = [1, 3, 3, 5, 7]
        D = [1, 5, 3, 7, 3]
        self.assertEqual(solution(A), True, 'incorrect response')
        self.assertEqual(solution(A), True, 'incorrect response')
        self.assertEqual(solution(B), True, 'incorrect response')
        self.assertEqual(solution(C), True, 'incorrect response')
        self.assertEqual(solution(D), False, 'incorrect response')

if __name__ == '__main__':
    unittest.main()