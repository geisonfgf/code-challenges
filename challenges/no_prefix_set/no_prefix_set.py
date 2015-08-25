"""
Problem Statement

Given N strings. Each string contains only lowercase letters from a−j(both
inclusive). The set of N strings is said to be GOOD SET if no string is
prefix of another string else, it is BAD SET.

For example, aab, abcde, aabcd is BAD SET because aab is prefix of aabcd.

Print GOOD SET if it satisfies the problem requirement. 
Else, print BAD SET and the first string for which the condition fails.

Input Format 
First line contains N, the number of strings in the set. 
Then next N lines follow, where ith line contains ith string.

Constraints 
1<=N<=105 
1 <= Length of the string <= 60

Output Format 
Output GOOD SET if the set is valid. 
Else, output BAD SET followed by the first string for which the condition
fails.

Sample Input00
7
aab
defgab
abcde
aabcde
cedaaa
bbbbbbbbbb
jabjjjad

Sample Output00
BAD SET
aabcde

Sample Input01
4
aab
aac
aacghgh
aabghgh

Sample Output01
BAD SET
aacghgh

Explanation 
aab is prefix of aabcde. So set is BAD SET and it fails at string aabcde.
"""

class Trie(object):

    def __init__(self):
        self.eos = False
        self.c = [None] * 10
        self.letters = "abcdefghij"

    def insert(self, s):
        if self.c[self.letters.index(s[0])] is None:
            self.c[self.letters.index(s[0])] = Trie()
            if len(s) == 1:
                self.c[self.letters.index(s[0])].eos = True
            else:
                return self.c[self.letters.index(s[0])].insert(s[1:])
        else:
            if len(s) == 1:
                return False
            if self.c[self.letters.index(s[0])].eos == True:
                return False
            return self.c[self.letters.index(s[0])].insert(s[1:])
        return True

def check_sets(sets):
    root = Trie()
    for prefix in prefixes:
        if not root.insert(prefix):
            good_set = False
            print "BAD SET"
            print prefix
            return
    print "GOOD SET"

prefixes = [str(raw_input()) for _ in xrange(int(input()))]
check_sets(prefixes)