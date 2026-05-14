def uniform_cost_search(start, goal, graph):
    frontier = [(0, start)]
    explored = []
    while frontier:
        cost, node = frontier.pop(0)
        if node == goal:
            return cost
        explored.append(node)
        for neighbor, neighbor_cost in graph[node].items():
            if neighbor not in explored:
                frontier.append((cost + neighbor_cost, neighbor))
    return None 