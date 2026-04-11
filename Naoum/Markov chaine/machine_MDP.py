from time import time


# ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
#                      Initialization
# ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
def T(s, a, s2):

    pass

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
# Value iteration
# ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
def valueIteration(EPSILON=1e-15, maxIter=200, VERBOSE=False):
    optPolicy = {};
    V = newV = {s: 0 for s in S}
    for iteration in range(maxIter):
        oldV = V;
        V = newV.copy()
        maxDiff = 0
        for s in S:
            maxV = -inf
            for a in actions[s]:
                Qsa = 0
                for s2 in S:
                    Tsas2 = T(s, a, s2)
                    Rsas2 = reward(s, a, s2)
                    Qsa += Tsas2 * (Rsas2 + GAMMA * oldV[s2])
                if Qsa > maxV:  # Is this the best action so far? If so, keep it
                    maxV = Qsa;
                    optPolicy[s] = a
            # Save the best of all actions for the state
            V[s] = maxV

            maxDiff = max(maxDiff, abs(oldV[s] - V[s]))
        if maxDiff < EPSILON: break

        if VERBOSE: print(iteration, "*" * 50); printVals(V)
    return V, optPolicy

# ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
GAMMA = 0.9
S = {'S0', 'S1', 'S2', 'S3'}
actions = {'E', 'N', 'R'}

R = {s: 0 for s in S} ;
V = {s: 0 for s in S} ;
inf = float("inf")

# ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
t1 = time()
V, optPolicy = valueIteration(EPSILON=1e-3, VERBOSE=True);
t2 = time()
print(t2 - t1)
# ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
print("~." * 20)
printVals(V)  # print(*sorted(V.items(), key=lambda x:x[0]),sep='\t', end="\n"*7)
print("~." * 20)
printPolicy(optPolicy)
