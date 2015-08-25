"""
Problem Statement

There are 2N values to represent nodes in a graph. They are divided into two
sets G and B. Each set has exactly N values. Set G is represent by
{G1,G2,...,GN}. G can take any value between 1 to N(inclusive). Set B is
represented by {B1,B2,⋯,BN}. B can take any value between N+1 to
2N(inclusive). Same value can be chosen any number of times.

Here (G1,B1),(G2,B2),...(GN,BN) represents the edges of the graph.

Your task is to print the number of vertices in the smallest and the largest
connected components of the graph.

Input Format

First line contains an integer N. 
Each of the next N lines contain two space-separated integers, ith line
contains Gi and Bi.

Constraints 

1<=N<=15000 
1<=Gi<=N 
N+1<=Bi<=2N

Output Format

Print two space separated integers, the number of vertices in the smallest
and the largest components.

Sample Input
5
1 6 
2 7
3 8
4 9
2 6

Sample Output
2 4

Explanation
The number of vertices in the smallest connected component in the graph is 2
i.e. either (3,8) or (4,9). 
The number of vertices in the largest connected component in the graph is 4
i.e. 1−2−6−7.
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
            self.parent[root_p] = root_q
            self.rank[root_q] += self.rank[root_p]
        else:
            self.parent[root_q] = root_p
            self.rank[root_p] += self.rank[root_q]

    def element_set_size(self, p):
        return self.rank[self.find(p)]

N = int(input())
uf = UnionFind(N*2)
for _ in xrange(N):
    p, q = map(int, raw_input().split(" "))
    uf.union(p-1, q-1)

vertices = sorted(list(set([uf.element_set_size(p) for p in xrange(N)])))
print vertices[1], vertices[-1]