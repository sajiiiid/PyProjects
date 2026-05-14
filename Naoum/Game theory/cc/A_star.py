def A_star(start, goal, graph, h):
    frontier = [(h[start], start)]
    explored = set()
    while frontier:
        cost, node = frontier.pop(0)
        if node == goal:
            return cost 
        explored.add(node)
        for neighbor, neighbor_cost in graph[node]:
            if neighbor not in explored:
                frontier.append((cost + neighbor_cost + h[neighbor], neighbor))
    return None 

h={'a':10, 'b':12, 'c':15, 'd':9, 'e':8, 'f':0, 'g':3, 'h':3}
G = {   'a':[('d',2)], 
        'b':[('c',5),('d',6)],
        'c':[('b',5),('e',8)],
        'd':[('a',2),('b',6),('e',1),('g',9), ('h',6)],
        'e':[('c',8),('d',1),('h',4)],
        'f':[('g',3)],
        'g':[('d',9),('f',3),('h',2)],
        'h':[('d',6),('e',4),('g',2)]
    } 

print(A_star('b', 'f', G, h))
