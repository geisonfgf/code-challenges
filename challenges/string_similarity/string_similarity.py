"""
Problem Statement

For two strings A and B, we define the similarity of the strings to be the
length of the longest prefix common to both strings. For example, the
similarity of strings "abc" and "abd" is 2, while the similarity of strings
"aaa" and "aaab" is 3.

Calculate the sum of similarities of a string S with each of it's suffixes.

Input: 
The first line contains the number of test cases T. Each of the next T lines
contains a string each.

Output: 
Output T lines containing the answer for the corresponding test case.

Constraints: 
1 <= T <= 10 
The length of each string is at most 100000 and contains only lower case
characters.

Sample Input:
2
ababaa
aa

Sample Output:
11  
3

Explanation: 
For the first case, the suffixes of the string are "ababaa", "babaa",
"abaa", "baa", "aa" and "a". The similarities of these strings with the
string "ababaa" are 6,0,3,0,1, & 1 respectively. Thus, the answer is
6 + 0 + 3 + 0 + 1 + 1 = 11.

For the second case, the answer is 2 + 1 = 3.
"""

def compute_prefix_array(prefix):
    result = [0] * len(prefix)
    matched = 0
    for i in xrange(1, len(prefix)):
        while matched > 0 and prefix[matched] != prefix[i]:
            matched = result[matched - 1]
        if prefix[matched] == prefix[i]:
            matched += 1
        result[i] = matched
    return result

def sum_suffix_similarities(s):
    prefix_array = compute_prefix_array(s)
    sum_array = []
    count = len(s)
    for i in xrange(len(s)):
        if prefix_array[i]:
            prefix_array[i] = prefix_array[prefix_array[i] - 1] + 1
        sum_array.append(prefix_array[i])
        count += sum_array[-1]
    return count

for i in xrange(int(raw_input())):
    print sum_suffix_similarities(raw_input())