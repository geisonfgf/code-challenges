""" Graph representation using a Dict """
graph = {0: set([1, 2]),
         1: set([0]),
         2: set([0]),
         3: set([4, 5]),
         4: set([3]),
         5: set([3])}

class ConectedComponents(object):

    def __init__(self, graph):
        self.graph = graph
        self.marked = [False] * len(graph.keys())
        self.id = [0] * len(graph.keys())
        self.count = 0

        for v in graph.keys():
            if not self.marked[v]:
                self.__dfs(graph, v)
                self.count += 1

    def connected(self, v, w):
        return self.id[v] == self.id[w]

    def __dfs(self, graph, start, visited=None):
        """ Depth-First Search interactive implementation """
        self.marked[start] = True
        self.id[start] = self.count

        if visited is None:
            visited = set()
        visited.add(start)
        for next in graph[start] - visited:
            self.__dfs(graph, next, visited)
        return visited

if __name__ == '__main__':
    cc = ConectedComponents(graph)
    print "Is connected 0 with 2? ", cc.connected(0, 2)
    print "Is connected 0 with 3? ", cc.connected(0, 3)
    print "Is connected 0 with 5? ", cc.connected(0, 5)
    print "Is connected 0 with 5? ", cc.connected(5, 3)
    print "Is connected 0 with 5? ", cc.connected(5, 4)
    print "Is connected 0 with 5? ", cc.connected(5, 0)
