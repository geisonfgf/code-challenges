"""
Problem Statement

People connect with each other in a social network. A connection between
Person I and Person J is represented as M I J. When two persons belonging
to different communities connect, the net effect is the merger of both
communities which I and J belongs to.

At the beginning, there are N people representing N communities. Suppose
person 1 and 2 connected and later 2 and 3 connected, then 1,2, and 3 will
belong to the same community.

There are two type of queries:

M I J=> communities containing person I and J merged (if they belong to
    different communities).

Q I=> print the size of the community to which person I belongs.

Input Format

The first line of input will contain integers N and Q, i.e. the number of
people and the number of queries.
The next Q lines will contain the queries.

Constraints:
1<=N<=105
1<=Q<=2x105

Output Format

The output of the queries.

Sample Input
3 6
Q 1
M 1 2
Q 2
M 2 3
Q 3
Q 2

Sample Output
1
2
3
3

Explanation
Initial size of each of the community is 1.
"""
class UnionFind(object):

    def __init__(self, n):
        self.parent = list(range(int(n)))
        self.rank = [1] * n
        self.count = n
 
    def find(self, p):
        N = len(self.parent)
        if p < 0 or p >= N:
            raise Exception("index {0} is not between 0 and {1}".format(p, N))
        while p != self.parent[p]:
            p = self.parent[p]
        return p

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p == root_q: return
        if self.rank[root_p] < self.rank[root_q]:
            self.parent[root_p] = root_q;
            self.rank[root_q] += self.rank[root_p]
        else:
            self.parent[root_q] = root_p;
            self.rank[root_p] += self.rank[root_q]

    def element_set_size(self, p):
        return self.rank[self.find(p)]


N, K = map(int, raw_input().split(" "))
uf = UnionFind(N)

for _ in xrange(K):
    line = raw_input().split(" ")
    if line[0] == "Q":
        person = int(line[1]) - 1
        print uf.element_set_size(person)
    elif line[0] == "M":
        person1, person2 = int(line[1]) - 1, int(line[2]) - 1
        uf.union(person1, person2)