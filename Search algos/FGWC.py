ENTITIES = frozenset({'F', 'C', 'G', 'W'})
S0 = frozenset({'F', 'C', 'G', 'W'})

def isValid(left):
    right = ENTITIES - left
    for bank in [left, right]:
        if 'F' not in bank:
            if 'G' in bank and ('W' in bank or 'C' in bank):
                return False
    return True

def isEnd(S): return S == frozenset()

def actions(left):
    right = ENTITIES - left
    result = []
    if 'F' in left:
        farmer_side = left
    else:
        farmer_side = right
    result.append(frozenset({'F'}))
    for entity in farmer_side - {'F'}:
        result.append(frozenset({'F', entity}))
    return result

def succ(left, action):
    if 'F' in left:
        return left - action
    else:
        return left | action

best = {'cost': float('inf'), 'path': None}

def backtrackingSearch(S, path, cost):
    global best
    if isEnd(S):
        if cost < best['cost']:
            best['cost'] = cost
            best['path'] = list(path)
        return
    # Pruning: no point continuing if already worse than best
    if cost >= best['cost']:
        return
    for a in actions(S):
        next_S = succ(S, a)
        if isValid(next_S) and next_S not in path:
            path.append(next_S)
            backtrackingSearch(next_S, path, cost + 1)
            path.pop()

backtrackingSearch(S0, [S0], 0)
print("Min cost:", best['cost'])
print("Path:")
for i, state in enumerate(best['path']):
    left = state
    right = ENTITIES - left
    print(f"  Step {i}: Left={set(left)} | Right={set(right)}")