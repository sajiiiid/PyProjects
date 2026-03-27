def isEnd(s): return s == 'Out'

def policyEvaluation(Pi, S, A, T, R, Gamma, maxIter=100, eps = 1e-6):
    V = {s: 0 for s in S}
    for t in range(maxIter):
        oldV = V.copy(); maxDiff = 0
        for s in S:
            v_s = 0
            for s2 in S:
                v_s += T.get( (s, Pi[s], s2), 0) * ( R.get( (s, Pi[s], s2), 0) + Gamma * oldV[s2] )
            V[s] = v_s
            maxDiff = max(maxDiff, abs(V[s] - oldV[s]))
        #print(*V.items(), sep='\n')
        if maxDiff < eps: break
    return V

S = {'In', 'Out'}; Gamma = 1
A = {'In': {'Stay', 'Quit'}, 'Out': set()}

T = {('In', 'Stay', 'In'): 2/3,
     ('In', 'Stay', 'Out'): 1/3,
     ('In', 'Quit', 'Out'): 1}

R = {('In', 'Stay', 'In'): 4,
     ('In', 'Stay', 'Out'): 4,
     ('In', 'Quit', 'Out'): 10}

Pi_stay = {'In' : 'Stay', 'Out' : None}
Pi_quit = {'In' : 'Quit', 'Out' : None}

V = policyEvaluation( Pi_stay, S, A, T, R, Gamma)
print(V)