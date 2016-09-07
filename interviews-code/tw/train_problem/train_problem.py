"""
Problem one: Trains
 
The local commuter railroad services a number of towns in Kiwiland. Because
of monetary concerns, all of the tracks are 'one-way.'  That is, a route from
Kaitaia to Invercargill does not imply the existence of a route from
Invercargill to Kaitaia.  In fact, even if both of these routes do happen to
exist, they are distinct and are not necessarily the same distance!
 
The purpose of this problem is to help the railroad provide its customers with
information about the routes.  In particular, you will compute the distance
along a certain route, the number of different routes between two towns, and
the shortest route between two towns.
 
Input:  A directed graph where a node represents a town and an edge represents
a route between two towns.  The weighting of the edge represents the distance
between the two towns.  A given route will never appear more than once, and
for a given route, the starting and ending town will not be the same town.
 
Output: For test input 1 through 5, if no such route exists, output
'NO SUCH ROUTE'.  Otherwise, follow the route as given; do not make any extra
stops!  For example, the first problem means to start at city A, then travel
directly to city B (a distance of 5), then directly to city C (a distance
of 4).

The distance of the route A-B-C.
The distance of the route A-D.
The distance of the route A-D-C.
The distance of the route A-E-B-C-D.
The distance of the route A-E-D.
The number of trips starting at C and ending at C with a maximum of 3 stops.
In the sample data below, there are two such trips: C-D-C (2 stops). and
C-E-B-C (3 stops).
The number of trips starting at A and ending at C with exactly 4 stops.
In the sample data below, there are three such trips: A to C (via B,C,D);
A to C (via D,C,D); and A to C (via D,E,B).
The length of the shortest route (in terms of distance to travel) from A to C.
The length of the shortest route (in terms of distance to travel) from B to B.
The number of different routes from C to C with a distance of less than 30.
In the sample data, the trips are: CDC, CEBC, CEBCDC, CDCEBC, CDEBC, CEBCEBC,
CEBCEBCEBC.
 
Test Input:
For the test input, the towns are named using the first few letters of the
alphabet from A to D.  A route between two towns (A to B) with a distance
of 5 is represented as AB5.
Graph: AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7
Expected Output:
Output #1: 9
Output #2: 5
Output #3: 13
Output #4: 22
Output #5: NO SUCH ROUTE
Output #6: 2
Output #7: 3
Output #8: 9
Output #9: 9
Output #10: 7
"""


import sys


"""
Graph Dictionary Representation
"""
graph = {'A': {'B': 5, 'D': 5, 'E': 7},
         'B': {'C': 4},
         'C': {'D': 8, 'E': 2},
         'D': {'C': 8, 'E': 6},
         'E': {'B': 3}}

graph2 = {'A': set(['B', 'D', 'E']),
          'B': set(['C']),
          'C': set(['D', 'E']),
          'D': set(['C', 'E']),
          'E': set(['B'])}

def distance(graphs, paths):
    NO_SUCH_ROUTE = 'NO SUCH ROUTE'
    result = 0
    for i in xrange(1, len(paths)):
        if graphs.has_key(paths[i - 1]) and graphs[paths[i - 1]].has_key(paths[i]):
            result += graphs[paths[i - 1]][paths[i]]
        else:
            return NO_SUCH_ROUTE
    return result

def bfs_paths(graph, start, goal):
    """ Return all possible paths between a start and goal vertex """
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for nxt in graph[vertex] - set(path):
            if nxt == goal and len(path) > 1:
                print nxt, goal, path
                yield path + [nxt]
            else:
                queue.append((nxt, path + [nxt]))

def main():
    """
    The distance of the route A-B-C.

    The distance of the route A-D.
    
    The distance of the route A-D-C.
    
    The distance of the route A-E-B-C-D.
    
    The distance of the route A-E-D.
    
    The number of trips starting at C and ending at C with a maximum of 3
    stops. In the sample data below, there are two such trips: C-D-C
    (2 stops). and C-E-B-C (3 stops).
    
    The number of trips starting at A and ending at C with exactly 4 stops. In
    the sample data below, there are three such trips: A to C (via B,C,D); A
    to C (via D,C,D); and A to C (via D,E,B).
    
    The length of the shortest route (in terms of distance to travel) from A to C.
    
    The length of the shortest route (in terms of distance to travel) from B to B.
    
    The number of different routes from C to C with a distance of less than 30.
    In the sample data, the trips are: CDC, CEBC, CEBCDC, CDCEBC, CDEBC, CEBCEBC, CEBCEBCEBC.
    """
    """print 'Expected 9, got:', distance(graph, ['A', 'B', 'C'])
    print 'Expected 5, got:', distance(graph, ['A', 'D'])
    print 'Expected 13, got:', distance(graph, ['A', 'D', 'C'])
    print 'Expected 22, got:', distance(graph, ['A', 'E', 'B', 'C', 'D'])
    print 'Expected NO SUCH ROUTE, got:', distance(graph, ['A', 'E', 'D'])"""
    #print 'Expected 2, got:', find_all_paths(graph, 'A', 'C')
    print list(bfs_paths(graph2, 'A', 'C'))
    
if __name__ == '__main__':
    sys.exit(int(main() or 0))