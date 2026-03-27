S0=({'F', 'G', 'W', 'C'}, set())

def isEnd(S):
    return S == (set(), {'F', 'G', 'W', 'C'})

def Action(S) :
    A, B = S
    FROM, ind = (A, 0) if 'F' in A else (B, 1)
    return [ (ind, {'F'} | {X}) for X in FROM]

def Successeur(S,a) :
    ind, E = a      ; A, B = S
    if ind == 0: return (A-E, B|E)
    return (A|E, B-E)

def isValid(S):
    A, B = S
    if 'F' not in A:
        if 'G' in A and ('W' in A or 'C' in A): return False
    if 'F' not in B:
        if 'G' in B and ('W' in B or 'C' in B): return False
    return True

def cost(S,a) :
    return 1

def backtrackSearch(S, path, best):
    if isEnd(S):
        if best['path'] is None or len(path) < len(best['path']):
            best['path'] = list(path)
        return

    if best['path'] is not None and len(path) >= len(best['path']):
        return

    for a in Action(S):
        next_S = Successeur(S, a)
        if isValid(next_S) and next_S not in path:
            path.append(next_S)
            backtrackSearch(next_S, path, best)
            path.pop()

def solve():
    best = {'path': None}
    backtrackSearch(S0, [S0], best)
    if best['path']:
        return best['path'], len(best['path']) - 1
    return None, 0