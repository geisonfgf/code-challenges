class UnionFind(object):

    def __init__(self, n):
        self.parent = list(range(int(n)))
        self.rank = [0] * n
        self.num = [1] * n
 
    def find(self, p):
        N = len(self.parent)
        if p < 0 or p >= N:
            raise Exception("index {0} is not between 0 and {1}".format(p, N))
        while p != self.parent[p]:
            p = self.parent[p]
        return p

    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p == root_q: return
        if self.rank[root_p] < self.rank[root_q]:
            self.parent[root_p] = root_q;
            self.num[root_q] += self.num[root_p]
        else:
            self.parent[root_q] = root_p;
            self.num[root_p] += self.num[root_q]
            if self.rank[root_p] == self.rank[root_q]:
                self.rank[root_p] += 1

    def element_set_size(self, p):
        return self.num[self.find(p)]


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