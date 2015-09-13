"""
Python Graph data structure

          A -- B
        / |    |\
       /  |    | \
      C   D    E  F
     /     \  /   |
    G       \/    /
    |------ H -- /


Graphs categories:
Dense  -> too many edges -> Best use of Adjacent List
Sparse -> too few edges  -> Best use of Edge List

Graph Walk:
A sequence of vertices where each adjacent pair is connected by an edge.
<A, B, F, H>

Simple Path: a walk in which no vertices (and thus no edges) are repeated.
Trail: a walk in which no edges are repeated.

Input:

Vertex List         Edge List
0 - A               [[0, 1, 5],
1 - B                [0, 2, 7],
2 - C                [0, 3, 3],
3 - D                [1, 4, 2],
4 - E                [1, 5, 10],
5 - F                [2, 6, 1],
6 - G                [3, 7, 11],
7 - H                [4, 7, 9],
                     [5, 7, 4],
                     [6, 7, 6]]

Time: O(|E|)
Space: O(|V|+|E|)

Vertex List         Adjacent List
                      | 0  1  2  3  4  5  6  7
0 - A               --------------------------
1 - B               0 | N  5  7  3  N  N  N  N
2 - C               1 | 5  N  N  N  2 10  N  N
3 - D               2 | 7  N  N  N  N  N  1  N
4 - E               3 | 3  N  N  N  N  N  N 11
5 - F               4 | N  2  N  N  N  N  N  9
6 - G               5 | N 10  N  N  N  N  N  4
7 - H               6 | N  N  1  N  N  N  N  6
                    7 | N  N  N  6 11  9  4  N

Time: O(V) 
Space: O(V^2)
"""

from collections import defaultdict

"""
Graph Class Representation
"""
class Graph:
  def __init__(self):
    self.nodes = set()
    self.edges = defaultdict(list)
    self.distances = {}

  def add_node(self, value):
    self.nodes.add(value)

  def add_edge(self, from_node, to_node, distance):
    self.edges[from_node].append(to_node)
    self.edges[to_node].append(from_node)
    self.distances[(from_node, to_node)] = distance


"""
Graph Dictionary Representation
"""
graph = {'1': {'2': 4, '3': 40},
         '2': {'1': 4, '3': 75, '4': 76},
         '3': {'1': 40, '2': 75, '4': 77},
         '4': {'2': 76, '3': 77}}


def find_path(graph, start, end, path=[]):
    path = path + [start] 
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None

def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not graph.has_key(start):
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

def dijsktra(graph, start, end):
    D, P = {}, {}
    
    for node in graph.keys():
        D[node] = -1
        P[node] = ""

    D[start] = 0
    unseen_nodes = graph.keys()

    while len(unseen_nodes) > 0:
        shortest = None
        node = ""
        for temp_node in unseen_nodes:
            if shortest is None or D[temp_node] < shortest:
                shortest = D[temp_node]
                node = temp_node

        unseen_nodes.remove(node)

        for child_node, child_value in graph[node].items():
            if D[child_node] < D[node] + child_value:
                D[child_node] = D[node] + child_value
                P[child_node] = node

    path = []
    node = end

    while not (node == start):
        if path.count(node) == 0:
            path.insert(0, node)
            node = P[node]
        else:
            break

    path.insert(0, start)

    return path

def distance(graph, path):
    distance = 0
    for i in xrange(1, len(path)):
        try:
            distance += graph[path[i]][path[i - 1]]
        except:
            return 0
    return distance