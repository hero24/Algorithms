"""
Minimum spanning tree
"""

# "To be successful, you must accept all challenges that come your way.
# You can’t just accept the ones you like." ~ Mike Gafka

def KruskalMST(graph):
    """
    Kruskals minimum spanning tree algorightm
    implementation in python.
    """
    result = []
    idx, ix = 0,0
    parents = []
    rank = []

    for node in graph.yield_nodes():
        parents.append(node)
        rank.append(0)

    node = [[node, conn] for node, conn in zip(graph.yield_nodes(),
                                               graph.yield_connections())]
    nodes = []
    for parent, conn in node:
        for i in range(len(conn)-1):
            if conn[i] is not False:
                nodes.append([parent, node[i][0], conn[i]])
    nodes.sort(key=lambda k: k[2])

    while ix < len(nodes)-1:
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
             if min_index:
                 result[min_index] = True
        for u, v in enumerate(graph.yield_connections()):
            if v > 0 and result[u] is False and key[u] > v:
                key[u] = v
                parent[u] = u
    return parent, result

