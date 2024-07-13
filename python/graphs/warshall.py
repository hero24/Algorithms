# "We do not stop playing because we grow old,
# we grow old because we stop playing!"
# ~ Benjamin Franklin

def roy_warshall(graph):
    """
    Roy-Warshall algorithm for matrix-based graphs
    that checks if connection between points on the graph
    is possible.
    """
    result = [[False for _ in range(len(graph))] for _ in range(len(graph))]
    nodes = [[key for key in graph.yield_nodes()] for _ in graph.yield_nodes()]
    i = 0
    for _, key in graph.yield_connections():
        for j in key:
            for k in range(len(nodes[i])):
                if nodes[i][k] == j:
                    nodes[i][k] = True
        for j in range(len(nodes[i])):
            if nodes[i][j] is not True:
                nodes[i][j] = False
        i += 1

    for x in range(len(nodes)):
        for y in range(len(nodes)):
            for z in range(len(nodes)):
                if result[y][z] is False:
                    yx = 0 if nodes[y][x] else 1
                    xz = 0 if nodes[x][z] else 1
                    result[y][z] = yx * xz
    return result


def floyd_warshall(graph):
    """
    Floyd-Warshall algorithm for matrix-based graphs
    that computes cheapest connections between points on the graph
    that are possible.
    """
    result = [[False for x in range(len(graph))] for _ in range(len(graph))]
    nodes = [[key for key in graph.yield_nodes()] for _ in graph.yield_nodes()]
    i = 0
    for nodea, key in graph.yield_connections():
        for j in key:
            for k in range(len(nodes[i])):
                if nodes[i][k] == j:
                    nodes[i][k] = graph.get_weight(nodea, j)
        for j in range(len(nodes[i])):
            if not isinstance(nodes[i][j], int):
                nodes[i][j] = float('inf')
        i += 1

    for x in range(len(nodes)):
        for y in range(len(nodes)):
            for z in range(len(nodes)):
                conns = [nodes[y][z],nodes[x][z], nodes[y][x]]
                filtered_conns = []
                for con in conns:
                    if con is not False:
                        filtered_conns.append(con)
                if len(filtered_conns) > 0:
                    result[y][z] = min(filtered_conns)
                else:
                    result[y][z] = False
    return result
