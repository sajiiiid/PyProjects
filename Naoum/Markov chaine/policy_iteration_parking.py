from time import time
import numpy as np

# ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
#                      Initialization
# ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
def T(s, a, s2):
    if s2 in P[s][a]: return P[s][a][s2]

    i, j = s  # get the coords of the current state
    allAct = {x: 0.1 for x in cross[a]}  # update liklyhood of the current actions
    allAct[a] = 0.8

    nbghrs = {}
    for act in allAct:  # for each possible action
        di, dj = d[act]  # get the next state
        X = (i + di, j + dj)
        if X not in S: X = (i, j)  # if the next stat out of the grid ==> rest to s
        nbghrs[X] = allAct[act] + nbghrs.get(X, 0)  # cummulatif probabilities
    P[s][a].update(nbghrs)
    return nbghrs.get(s2, 0)  # nbghrs


# ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
def reward(s, a, s2): return R[s2]

# ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
def printVals(V):
    for i in range(3):
        for j in range(4):
            print(f"{V.get((i, j), -inf): 7.3f}", end='\t')
        print()

# ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
def printPolicy(V):
    for i in range(3):
        for j in range(4):
            print(V.get((i, j), '#'), end='\t')
        print()

# ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
# Policy evaluation
# ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
def policyEvaluation(Pi, EPSILON=1e-4, maxIter=200, VERBOSE=False):
    V = {s: 0 for s in S}
    for iteration in range(maxIter):
        oldV = V.copy()
        maxDiff = 0
        for s in S:
            a = Pi[s]
            curV = 0
            for s2 in S:
                curV += T(s, a, s2) * (reward(s, a, s2) + GAMMA * oldV[s2])
            V[s] = curV

            maxDiff = max(maxDiff, np.abs(oldV[s] - V[s]))

        if maxDiff < EPSILON: break
        if VERBOSE: print(iteration, "*" * 50); printVals(V)
    return V

# ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
# Policy iteration
# ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
def policyIteration(EPSILON=1e-15, maxIter=200, VERBOSE=False):
    optPolicy = {s: next(iter(actions[s])) for s in S}
    V = {s: 0 for s in S}

    for iteration in range(maxIter):
        # Policy evaluation
        V = policyEvaluation(optPolicy, EPSILON=EPSILON, maxIter=maxIter, VERBOSE=False)

        # Policy improvement
        policyStable = True
        for s in S:
            oldAction = optPolicy[s]
            bestAction = oldAction
            bestValue = float("-inf")

            for a in actions[s]:
                curV = 0
                for s2 in S:
                    curV += T(s, a, s2) * (reward(s, a, s2) + GAMMA * V[s2])

                if curV > bestValue:
                    bestValue = curV
                    bestAction = a

            optPolicy[s] = bestAction
            if bestAction != oldAction:
                policyStable = False

        if VERBOSE:
            print(iteration, "*" * 50)
            printVals(V)
            printPolicy(optPolicy)

        if policyStable:
            break

    return V, optPolicy


# ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
GAMMA = 0.9; GREEN = (0, 3); RED = (1, 3); BLACK = (1, 1)
S = {(i, j) for j in range(4) for i in range(3)} - {BLACK}

actions = {s: ('U', 'D', 'L', 'R') for s in S};  # actions[ (0, 0) ] = ('D', 'R')  ; actions[ (2,3) ] = ('U', 'L')
cross = {'U': ('L', 'R'), 'D': ('L', 'R'), 'L': ('U', 'D'), 'R': ('U', 'D')}
d = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

R = {s: 0 for s in S}; R[GREEN] = 1; R[RED] = -100
V = {s: 0 for s in S}; V[GREEN] = 1; V[RED] = -100  # V = R.copy( )

P = {s: {a: {} for a in actions[s]} for s in S}
inf = float("inf")

# RandomPolicy = { s: np.random.choice( actions[s] ) for s in S}
# ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
t1 = time();
V, optPolicy = policyIteration(EPSILON=1e-3, VERBOSE=True);
t2 = time()
print(t2 - t1)
# ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
print("~." * 20);
printVals(V)  # print(*sorted(V.items(), key=lambda x:x[0]),sep='\t', end="\n"*7)
print("~." * 20);
printPolicy(optPolicy)

