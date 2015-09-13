"""
An airline needs your help to fly the shortest path between two cities.
There are airports and airways connecting the airports. There is at most
one airway between any two different airports. There is no airway connecting
an airport to itself. Travel time for an airway is the same for both
directions. At every airport there is an operating mode that is either Alpha
or Beta at any moment. The operating mode of each airport alternates
periodically: Alpha for certain duration and then Beta for another duration.
Airline traffic is permitted to travel the airway between any two airports,
if and only if the operating modes at both airports are the same at the moment
of departing from one airport for the other. If an airplane arrives at an
airport just at the moment the operating mode switches it must consider the
new operating mode. Airplanes are allowed to wait at the airports. You are
given the airports map which shows:

the travel times for all airways (integers)
the durations of the two operating modes at each airport (integers)
and the initial operating mode and the remaining time (integer) for this
operating mode to change at each airport.
Your task is to find a path which takes the minimum time from a given source
airport to a given destination airport for an airplane when the traffic
starts. In case more than one such path exists you are required to report
only one of them.

Input

The first line contains two numbers: The ID (integer) of the source airport
and the ID (integer) of the destination airport.

The second line contains two numbers: N and M (2<=N<=300, 1<=M<=14000).

The following N lines contain information on N airports: The i+2'th line of
the input file holds information about the airport i: mi, rim, tia, tib
where mi is either A for Alpha mode and B for Beta mode, rim is the remaining
time for that airport in the current operating mode (mi), tia is the total
duration of the Alpha mode for airport i, tib is the total duration of Beta
mode for airport i
(1<=tia<=100, 1<=tib<=100, 1<=rim<=(tia if mi==A, tib if mi==B).

The next M lines (1<=M<=14000) represent the airways between the different
airports in the format i, j, lij (1<=lij<=100) where i and j are the
connected airports for that airway and lij is the time required to move from
airport i to j using the airway that connects i and j.

Output

If a path exists:

The first line will contain the time taken by a minimum-time path from the
source airport to the destination airport.

Second line will contain the list of airports that construct the minimum-time
path you have found. You have to write the airports to the output file in the
order of travelling. Therefore the first integer in this line must be the
id-number of the source airport and the last one the id-number of the
destination airport.

If a path does not exist:
A single line containing only the integer 0.

Examples:
 
Test case 1:        Test case 2:        Test case 3:
Input:              Input:              Input:
1 4                 4 8                 2 5
4 5                 10 15               6 6
A 2 16 99           A 30 60 90          A 2 10 10
B 6 32 13           B 4 30 15           B 10 10 10
B 2 87 4            B 12 50 50          A 4 20 18
B 38 96 49          A 1 10 20           B 5 15 12
1 2 4               A 15 30 18          A 9 18 52
1 3 40              B 9 18 17           B 15 46 32
2 3 75              A 22 23 59          1 2 12
2 4 76              A 15 39 3           1 3 32
3 4 77              A 5 10 10           1 6 18
                    B 9 51 99           2 3 69
                    1 2 89              2 6 61
                    1 3 32              4 5 75
                    2 3 47
                    2 4 33
                    2 5 53
                    1 6 84
                    4 6 62
                    6 9 42
                    1 8 26
                    1 9 41
                    8 10 18
                    5 10 82
                    4 9 71
                    2 8 59
                    6 8 82


Output:             Output:             Output:
127                 108                 0
1 2 4               4 2 8
"""

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

source, destination = map(int, raw_input().split(" "))
N, M = map(int, raw_input().split(" "))
graph = {}
vertex_list, adjacent_list = {}, []

for i in xrange(1, N+1):
    mi, rim, tia, tib = raw_input().split(" ")
    graph1[str(i)] = {}

for i in xrange(M):
    i, j, lij = map(int, raw_input().split(" "))
    graph1[str(i)][str(j)] = lij
    graph1[str(j)][str(i)] = lij

path = dijsktra(graph1, str(source), str(destination))
distance = distance(graph1, path)
print path
print distance
print graph1

"""
Vertex List
{
  1: ['A', 2, 16, 99],
  2: ['B', 6, 32, 13],
  3: ['B', 2, 87, 4],
  4: ['B', 38, 96, 49]
}

Adjacent List
[
  [1, 2, 4],
  [1, 3, 40],
  [2, 3, 75],
  [2, 4, 76],
  [3, 4, 77]
]

       4
    1-----2
    |    /|
    |   / |
  40|75/  |76
    | /   |
    |/    |
    3-----4
       77

"""