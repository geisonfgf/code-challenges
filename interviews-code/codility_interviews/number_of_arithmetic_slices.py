"""
A sequence of numbers is called arithmetic if it consists of at least three
elements and if the difference between any two consecutive elements is the
same. For example, these are arithmetic sequences:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9

The sequence [1, 1, 2, 5, 7] is not arithmetic.

A zero-indexed array A consisting of N numbers is given. A slice of that array
is any pair of integers (P, Q) such that 0 <= P < Q < N.

A slice (P, Q) of array A is called arithmetic if the sequence:
A[P], A[P+1], ..., A[Q-1], A[Q]

is arithmetic. In particular, this means that P + 1 < Q.

Write a function:

def solution(A)

that, given array A consisting of N numbers, returns the number of
arithmetic slices in A. The function should return -1 if the result exceeds
1,000,000,000.

For example, given array A such that:
A[0] = -1
A[1] = 1
A[2] = 3
A[3] = 3
A[4] = 3
A[5] = 2
A[6] = 1
A[7] = 0

the function should return 5 because there are five arithmetic slices of that
array, namely:

(0, 2) (2, 4) (4, 6) (4, 7) (5, 7)

Assume that:

- N is an integer within the range [0..60,000];
- each element of array A is an integer within the range
[-2,147,483,648..2,147,483,647].

Complexity:

- expected worst—case time complexity is 0(N);
- expected worst—case space complexity is 0(N), beyond input
storage (not counting the storage required for input
arguments).

Elements of input arrays can be modiﬁed.
"""

def solution(A):
    arr_length = len(A)

    if arr_length < 3:
        return 0

    start_slice, number_slices = 0, 0

    while start_slice < arr_length - 2:
        end_slice = start_slice + 1
        arithmetic_difference = A[end_slice] - A[start_slice]

        while end_slice < arr_length - 1 and A[end_slice + 1] - A[end_slice] == arithmetic_difference:
            end_slice += 1

        length_slice = end_slice - start_slice + 1

        if length_slice >= 3:
            number_slices += (length_slice - 2) * (length_slice - 1) / 2

        start_slice = end_slice

    if number_slices > 1000000000:
        return -1

    return number_slices

if __name__ == '__main__':
    print "Expect 5, result: ", solution([-1, 1, 3, 3, 3, 2, 1, 0])