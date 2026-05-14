#=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~

                                        ##  Shapley Value :  ##

#=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~

def factorielle(N):
    if N == 0 or N == 1 :
        return 1
    else : return N * factorielle(N-1)

#=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
    
def v( S ): return int( sum( votes[x] for x in S ) >=51 ) 

#=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~

def shapley_value(N,v,S):
    phi= { player:0 for player in N }
    n = len(N)
    for i in N:
        phi_i=0
        for s in S :
            if i not in s: phi_i += ( 1 / factorielle(n) ) *factorielle(len(s)) * factorielle(n-len(s)-1) * (v(s|{i}) - v(s))
        phi[i] = phi_i*100
    return phi

#=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~

L = [ chr(ord('A')+i) for i in range( 4) ]
N = set( L )
votes = { 'A':45 , 'B':25 , 'C':15 , 'D':15 }

S = [0] * ( 1 << len(N) )
for i in range(len(S)):
    S[ i ] = { L[j] for j in range( len ( N )) if ( i >> j ) % 2 }

Phi = shapley_value(N,v,S)

#=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~

for k,v in Phi.items():
    print( f'player : { k } , value : { v } ' )
print()
print(f'la somme des phi_i : {round(sum(Phi.values()),1)}')
