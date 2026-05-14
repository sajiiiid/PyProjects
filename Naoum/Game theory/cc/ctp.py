inf = float('inf')

def minmax(position, depth, alpha, beta, maximizingPlayer):
    # Base case: if depth is 0 or node is a leaf, return the value and its path
    if isinstance(position, int) or depth == 0:
        return position, [position]

    if maximizingPlayer:
        maxEval = -inf
        bestPath = []
        # Iterate over all children nodes
        for child in position:
            val, path = minmax(child, depth - 1, alpha, beta, False)
            # Update max value and track the best path taking this branch
            if val > maxEval:
                maxEval = val
                bestPath = [position] + path
            alpha = max(alpha, val)
            print(f"Winning Value: {maxEval} maximizing player")
            # Alpha-beta pruning
            if beta <= alpha:
                break
        return maxEval, bestPath

    else:
        minEval = inf
        bestPath = []
        # Iterate over all children nodes
        for child in position:
            val, path = minmax(child, depth - 1, alpha, beta, True)
            # Update min value and track the best path taking this branch
            if val < minEval:
                minEval = val
                bestPath = [position] + path
            beta = min(beta, val)
            print(f"Winning Value: {minEval} minimizing player")
            # Alpha-beta pruning
            if beta <= alpha:
                break
        return minEval, bestPath

tree = [
    6,
    [3,
        [5, [5, [5], [6]], [4, [7], [4], [5]]],
        [3, [3, [3]]]
    ],
    [6,
        [6, [6, [6]], [6, [6], [9]]],
        [7, [7, [7]]]
    ],
    [5,
        [5, [5, [5]]],
        [8, [8, [9], [8]], [6, [6]]]
    ]
]

depth = 5 #max, min, max, min, max
eval, path = minmax(tree, depth, -inf, inf, True)
print(f"\nFinal winning Value: {eval}")
print(f"Winning Strategy Path: {path}")



Final winning Value: 6
Winning Strategy Path: [[6, [3, [5, [5, [5], [6]], [4, [7], [4], [5]]], [3, [3, [3]]]], [6, [6, [6, [6]], [6, [6], [9]]], [7, [7, [7]]]], [5, [5, [5, [5]]], [8, [8, [9], [8]], [6, [6]]]]], 6]
