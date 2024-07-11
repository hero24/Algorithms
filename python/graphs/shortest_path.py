# "Life is short, art long, opportunity fleeting,
# experience treacherous, judgment difficult."
# ~ Hippocrates

NEG_CYCLE = True

def dikstra(graph, statring_point):
    """
    Dijkstra shortest path algorithm
    """
    previous = {}
    unvisited = [node for node in graph.yield_nodes()]
    shortest = {node:float('inf') for node in unvisited}
    shortest[statring_point] = 0
    while unvisited:
        current = None
        for node in unvisited:
            if current is None:
                current = node
            elif shortest[node] < shortest[current]:
                current = node
        neighbours = graph.adjacent(current)
        for neighbor in neighbours:
            value = shortest[current] + graph.get_weight(current, neighbor)
            if value < shortest[neighbor]:
                shortest[neighbor] = value
                previous[neighbor] = current
        unvisited.remove(current)
    return previous, shortest


def bellman_ford(graph, starting_point):
    """
    Shortest path algorithm that accounts for
    negative cycles. Returns True if graph contains
    negative.
    """
    inf = float("inf")
    unvisited = [node for node in graph.yield_nodes()]
    shortest = {node:inf for node in unvisited}
    shortest[starting_point] = 0
    for node in graph.yield_nodes():
        for neighbour in graph.neighbours(node):
            weight = graph.get_weight(node, neighbour)
            n_weight = shortest[node] + weight
            if shortest[node] != inf and n_weight < shortest[neighbour]:
                shortest[neighbour] = shortest[node] + weight
    for node in graph.yield_nodes():
        for neighbour in graph.neighbours(node):
            weight = shortest[node] + graph.get_weight(node, neighbour)
            if shortest[node] != inf and weight < shortest[node]:
                return NEG_CYCLE
    return shortest
