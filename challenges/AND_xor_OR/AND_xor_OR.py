"""
Problem Statement
Given an array A[] of N distinct elements. Let A and B be the smallest and
the next smallest element in the interval [L,R] where 1 <= L < R <= N.

Si=(((A∧B)⊕(A∨B))∧(A⊕B)).

where ∧,∨,⊕, are the bitwise operators AND, OR and XOR respectively. 
Your task is to find the maximum possible value of Si.

Input Format

First line contains integer N. 
Second line contains N integers, representing elements of the array A[].

Constraints 
1<N<=106 
1<=Ai<=109

Output Format
Print the value of maximum possible value of Si.

Sample Input
5
9 6 3 5 2

Sample Output
15

Explanation
Consider the interval [1,2] the result will be maximum. 
(((9∧6)⊕(9∨6))∧(9⊕6))=15
"""

N = int(input())
A = map(int, raw_input().split())

max_value = 0
stack = []
stack.append(A[0])

for i in xrange(1, N):
    L = A[i]
    while stack and L < stack[-1]:
        R = stack.pop()
        tmp_max_val = L ^ R
        if tmp_max_val > max_value:
            max_value = tmp_max_val
    if stack:
        R = stack[-1]
        tmp_max_val = L ^ R
        if tmp_max_val > max_value:
            max_value = tmp_max_val
    stack.append(L)

print max_value