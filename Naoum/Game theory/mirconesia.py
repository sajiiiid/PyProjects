L = [chr(ord('A') + i) for i in range(4)] ; N = set(L)
Votes = {'A' : 45, 'B' : 25, 'C' : 15, 'D' : 15}
Phi = { player : 0 for player in N}; print(Phi)

def V( S ):
    return int(sum(Votes[x] for x in S) >= 51)
factorial= {0:1, 1:1}
def fact(n) :
    if n in factorial : return factorial[n]
    p=1
    for i in range(2, n+1) : p *= i
    factorial[n] = p
    return p

all_S = [0] * (1 << len(N)) # there is 2^N coalition
for i in range(len(all_S)) : # range(2**len(N)) : preparer tou les coalitions
    all_S[i] = {L[j] for j in range(len(N)) if (i >> j) % 2} # tout les combinaisons possible
    #print(all_S[i], V(all_S[i]))

f_N = fact(len(N))
for i in Phi : # calcule SHAPLEY VALUE for player i
    somme = 0
    for S in all_S:
        if i in S : continue
        somme += fact(len(S)) * fact(len(N) - len(S) - 1) * ( V(S | {i}) - V(S))
        print(S, V(S))
    Phi[i] = somme/f_N
    print(f"pour le joueur {i}:", {Phi[i]})