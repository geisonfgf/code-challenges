""" Graph representation using a Dict """
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

""" Depth-First Search """
def dfs(graph, start):
    """ Depth-First Search interactive implementation """
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

dfs(graph, 'A') # {'E', 'D', 'F', 'A', 'C', 'B'}

def dfs_paths(graph, start, goal):
    """ Return all possible paths between a start and goal vertex """
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

list(dfs_paths(graph, 'A', 'F')) # [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]

def dfs_recursive(graph, start, visited=None):
    """ Depth-First Search recursive implementation """
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs_recursive(graph, next, visited)
    return visited

dfs_recursive(graph, 'C') # {'E', 'D', 'F', 'A', 'C', 'B'}

def dfs_paths_recursive(graph, start, goal, path=None):
    """ Return all possible paths between a start and goal vertex """
    if path is None:
        path = [start]
    if start == goal:
        yield path
    for next in graph[start] - set(path):
        yield from dfs_paths_recursive(graph, next, goal, path + [next])

list(dfs_paths_recursive(graph, 'C', 'F')) # [['C', 'F'], ['C', 'A', 'B', 'E', 'F']]