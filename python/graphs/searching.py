
# "Success is going from failure to failure
# without losing your enthusiasm."
# ~ Winston Churchill

def _make_matrix(graph):
    i = 0
    nodes = [[node for node in graph.yield_nodes()] for _ in graph.yield_nodes()]
    for v, node in graph.yield_connections():
        for j in node:
            for k in range(len(nodes[i])):
                if nodes[i][k] == j:
                    nodes[i][k] = j
        for j in range(len(nodes[i])):
            if not isinstance(nodes[i][j], str):
                nodes[i][j] = False
        i += 1
        return nodes


def search(value, item):
    return value == item


def DFS(graph, item, searchf=search, i=-1, seen=[]):
    """
    Depth-first search
    """
    if i == -1:
        for i in range(len(graph)):
            seen.append(False)
        graph = _make_matrix(graph)
        i = 0
    seen[i] = True
    for k in range(0, len(graph)):
        if searchf(graph[i][k], item):
            return True, i
        if graph[i][k] is not False and seen[k] is False:
            return DFS(graph, item, searchf, k, seen)
    return False


def BFS(graph, item, searchf=search):
    i = 0
    queue = [i]
    seen = [False for x in range(len(graph))]
    matrix = _make_matrix(graph)
    s = 0
    while len(queue) > 0:
        s = queue.pop(0)
        seen[s] = True
        for k in range(len(graph)):
            if searchf(matrix[s][k], item):
                return True, k
            if matrix[s][k] is not False and seen[k] is False:
                seen[k] = True
                queue.append(k)
    return False
