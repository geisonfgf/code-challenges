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
    ans = S
    stack = []
    sub = ans[-2:]
    stack.append([ans, sub, ""])
    while stack:
        ans, sub, left = stack.pop()
        if sub == "AB" or sub == "BA":
            ans = ans[:-2] + "AA" + left
            sub = ans[-2:]
            stack.append([ans, sub, left])
        elif sub == "CB" or sub == "BC":
            ans = ans[:-2] + "CC" + left
            sub = ans[-2:]
            stack.append([ans, sub, left])
        elif sub == "AA":
            ans = ans[:-2] + "A" + left
            sub = ans[-2:]
            stack.append([ans, sub, left])
        elif sub == "CC":
            ans = ans[:-2] + "C" + left
            sub = ans[-2:]
            stack.append([ans, sub, left])
        elif (ans[-2:] == "AC" or ans[-2:] == "CA") and len(ans) > 2:
            if len(ans) > 3:
                sub = ans[:2]
                left = ans[3:]
                ans = ""
                stack.append([ans, sub, left])
            else:
                sub = ans[:2]
                left = ans[-1]
                ans = ""
                stack.append([ans, sub, left])
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
print "Expected answer: AC"
print "My answer: ", solution("BACBAC")