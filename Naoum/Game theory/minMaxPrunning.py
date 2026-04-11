inf = float('inf')
def minmax(position, depth, alpha, beta, maximizingPlayer):
    if depth == 0:
        return position

    if maximizingPlayer:
        maxEval = -inf
        for child in position:
            eval = minmax(child, depth-1, alpha, beta, False)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return maxEval

    else :
        minEval = inf
        for child in position:
            eval = minmax(child, depth-1, alpha, beta, True)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return minEval