"""
The input is a string having only A, B or C.

Apply the rules below until the string not match more any rule and return
the string modified.

Rules:
    "AB" becomes "AA"
    "BA" becomes "AA"
    "CB" becomes "CC"
    "BC" becomes "CC"
    "AA" becomes "A"
    "CC" becomes "C"

Input:
    "AABCC"

Output:
    "AC"

Time complexity O(N)
Space complexity O(N)
"""

def solution(S):
    aux_string, ans = "", ""

    for i in xrange(len(S) - 1):
        sub = S[i] + S[i + 1]
        if sub == "AB" or sub == "BA" or sub == "AA":
            aux_string += "A"
        elif sub == "CB" or sub == "BC" or sub == "CC":
            aux_string += "C"
        elif sub == "AC" or sub == "CA":
            aux_string += sub

    for i in xrange(len(aux_string) - 1):
        if aux_string[i] != aux_string[i + 1]:
            ans += aux_string[i]
        if i + 2 == len(aux_string):
            ans += aux_string[i + 1]
            break

    return ans

print "Input: AABCC"
print "Expected answer: AC"
print "My answer: ", solution("AABCC")
print ""
print "Input: AAAABCC"
print "Expected answer: AC"
print "My answer: ", solution("AAAABCC")
print ""
print "Input: ABCABC"
print "Expected answer: ACAC"
print "My answer: ", solution("ABCABC")
print ""
print "Input: CBACBA"
print "Expected answer: CACA"
print "My answer: ", solution("CBACBA")
print ""
print "Input: BACBAC"
print "Expected answer: ACAC"
print "My answer: ", solution("BACBAC")
print ""
print "Input: BACAAC"
print "Expected answer: ACAC"
print "My answer: ", solution("BACAAC")
print ""
print "Input: BACCAC"
print "Expected answer: ACAC"
print "My answer: ", solution("BACCAC")
print ""
print "Input: ACCACAC"
print "Expected answer: ACACAC"
print "My answer: ", solution("ACCACAC")