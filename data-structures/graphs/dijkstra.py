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

if __name__ == "__main__":
    graph1 = {'1': {'2': 4, '3': 40},
              '2': {'1': 4, '3': 75, '4': 76},
              '3': {'1': 40, '2': 75, '4': 77},
              '4': {'2': 76, '3': 77}}

    graph2 = {'1': {'2': 89, '3': 32, '6': 84},
              '2': {'1': 89, '3': 47, '4': 33, '5': 53},
              '3': {'1': 32, '2': 47},
              '4': {'2': 33, '6': 62, '9': 71},
              '5': {'2': 53, '10': 82},
              '6': {'1': 84, '4': 62, '8': 82, '9': 42},
              '7': {},
              '8': {'1': 26, '2': 59, '6': 82, '10': 18},
              '9': {'1': 41, '4': 71, '6': 42},
              '10': {'5': 82, '8': 18}}

    graph3 = {'1': {'2': 12, '3': 32, '6': 18},
              '2': {'3': 69, '6': 61},
              '3': {'1': 32, '2': 69},
              '4': {'5': 75},
              '5': {'4': 75},
              '6': {'1': 18, '2': 77}}

    path1 = dijsktra(graph1, '1', '4')
    path2 = dijsktra(graph2, '4', '8')
    path3 = dijsktra(graph3, '2', '5')
    distance1 = distance(graph1, path1)
    distance2 = distance(graph2, path2)
    distance3 = distance(graph3, path3)
    print path1, distance1
    print path2, distance2
    print path3, distance3