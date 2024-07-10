# "Life is short, art long, opportunity fleeting,
# experience treacherous, judgment difficult."
# ~ Hippocrates

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