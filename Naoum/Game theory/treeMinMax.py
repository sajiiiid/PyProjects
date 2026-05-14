inf = float('inf')

def minmax(position, depth, alpha, beta, maximizingPlayer):
    # Handle leaf nodes (integers)
    if isinstance(position, int) or depth == 0:
        return position, [position]

    if maximizingPlayer:
        maxEval = -inf
        bestPath = []
        for child in position:
            val, path = minmax(child, depth - 1, alpha, beta, False)
            if val > maxEval:
                maxEval = val
                bestPath = [position] + path
            alpha = max(alpha, val)
            print(f"Winning Value: {maxEval}")
            print(f"Winning Strategy Path: {bestPath}")
            if beta <= alpha:
                break
        return maxEval, bestPath
    else:
        minEval = inf
        bestPath = []
        for child in position:
            val, path = minmax(child, depth - 1, alpha, beta, True)
            if val < minEval:
                minEval = val
                bestPath = [position] + path
            beta = min(beta, val)
            print(f"Winning Value: {minEval}")
            print(f"Winning Strategy Path: {bestPath}")
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

depth = 5
eval, path = minmax(tree, depth, -inf, inf, True)
print(f"Winning Value: {eval}")
print(f"Winning Strategy Path: {path}")