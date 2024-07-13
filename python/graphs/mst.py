"""
Minimum spanning tree
"""


# "To be successful, you must accept all challenges that come your way.
# You can’t just accept the ones you like." ~ Mike Gafka

def _make_matrix(graph):
    """
    helper function for translating graph into
    graph matrix
    """
    i = 0
    nodes = [[node for node in graph.yield_nodes()] for _ in graph.yield_nodes()]
    for v, node in graph.yield_connections():
        for j in node:
            for k in range(len(nodes[i])):
                if nodes[i][k] == j:
                    nodes[i][k] = graph.get_weight(v, j)
        for j in range(len(nodes[i])):
            if not isinstance(nodes[i][j], int):
                nodes[i][j] = float('inf')
        i += 1
        return nodes


def KruskalMST(graph):
    """
    Kruskals minimum spanning tree algorithm
    implementation in python.
    """
    result = []
    idx, ix = 0, 0
    parents = []
    rank = []

    for node in graph.yield_nodes():
        parents.append(node)
        rank.append(0)
    node = [[node, conn] for node, conn in zip(graph.yield_nodes(),
                                               graph.yield_connections())]
    nodes = []
    for parent, conn in node:
        for i in range(len(conn[1])):
            weight = graph.get_weight(parent, conn[1][i])
            if weight is False:
                weight = float('inf')
            nodes.append([parent, conn[1][i], weight])
    nodes.sort(key=lambda k: k[2])
    while ix < len(nodes) - 1:
        node, vertex, weight = nodes[idx]
        idx += 1
        parent, pid = graph.parent(node)
        parent2, pidx = graph.parent(vertex)
        if parent != parent2:
            ix += 1
            result.append([node, vertex, graph.get_weight(node, vertex)])
            if rank[pid] < rank[pidx]:
                parents[pid] = parent2
            elif rank[pid] > rank[pidx]:
                parents[pidx] = parent
            else:
                parents[pidx] = parent
                rank[pid] += 1
    min_cost = 0
    for *_, weight in result:
        min_cost += weight
    return result, min_cost


def PrimMST(graph):
    """
    Prim's minimum spanning tree algorithm
    """
    nodes = _make_matrix(graph)
    node_names = [node for node in graph.yield_nodes()]
    key = [float('inf') for _ in range(len(graph))]
    parent = [None for _ in range(len(graph))]
    result = [False for _ in range(len(graph))]
    key[0] = 0
    parent[0] = -1

    for edge_idx in range(len(graph)):
        minv = float('inf')
        min_index = False
        for vertex in range(len(graph)):
            if key[vertex] < minv and result[vertex] is False:
                minv = key[vertex]
                min_index = vertex
        else:
                result[min_index] = True
        for u, v in enumerate(nodes):
            for vertex in v:
                if v[0] > 0 and result[u] is False and key[u] > v[0]:
                    key[u] = vertex
                    parent[u] = node_names[u]
    return parent, result
