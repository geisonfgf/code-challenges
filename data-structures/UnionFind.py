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