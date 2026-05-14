capacity_A = 5
capacity_B = 3
S0 = (0, 0)  # Both jugs start empty

def isEnd(S):
    A, B = S
    return A == 4 # We win if Jug A has exactly 4 gallons. We don't care about B.

def Actions(S):
    return [
        'Fill A', 'Fill B',
        'Empty A', 'Empty B',
        'Pour A to B', 'Pour B to A'
    ]

def Succ(S, a):
    A, B = S

    if a == 'Fill A':
        return (capacity_A, B)  # A becomes 5, B stays the same

    if a == 'Fill B':
        return (A, capacity_B)  # A stays the same, B becomes 3

    if a == 'Empty A':
        return (0, B)  # A drops to 0, B stays the same

    if a == 'Empty B':
        return (A, 0)  # A stays the same, B drops to 0

    if a == 'Pour A to B':
        # The magic math:
        transfer = min(A, capacity_B - B)
        return (A - transfer, B + transfer)

    if a == 'Pour B to A':
        # Same logic, in reverse:
        transfer = min(B, capacity_A - A)
        return (A + transfer, B - transfer)

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
