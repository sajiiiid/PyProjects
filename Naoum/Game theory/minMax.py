inf = float('inf')
def minmax(position, depth, maximizingPlayer):
    if depth == 0:
        return position

    if maximizingPlayer:
        maxEval = -inf
        for child in position:
            eval = minmax(child, depth-1, False)
            maxEval = max(maxEval, eval)
        return maxEval

    else :
        minEval = inf
        for child in position:
            eval = minmax(child, depth-1, True)
            minEval = min(minEval, eval)
        return minEval