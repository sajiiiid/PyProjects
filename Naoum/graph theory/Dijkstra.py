#~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
# UIASS > EIA > GISIBA1 > naoum.mohamed@gmail.com
#
#
# Théorie des graphes > Correction TP 03 >
# Algorithme de Dijkstra pour le plus court chemin
#
#~=~=~=~=~=~=~=~==~=~
inf = float('inf')

G = { #representation du graphe G avec un dictionnaire #abcdefgh
    # Les cles du dict sont les sommets de G
    'a': [('d', 2)], # la valeur de la clé est une liste de tuples
    'b': [('c', 5), ('d', 6)], # pr chaque tuple la 1er valeur designe le sommet d'arrivée
    'c': [('b',5), ('e',8)], # la deuxième valeur represente le coût de cette liaison
    'd': [('a',2), ('b',6), ('e',1), ('g',9), ('h',6)],
    'e': [('c',8), ('d',1), ('h',4)],
    'f':[('g',3)],
    'g': [('d',9), ('f',3), ('h',2)],
    'h': [('d',6), ('e', 4), ('g', 2)]
}
def dijkstra(G,S):
    D={v:inf for v in G}; D[S]=0
    visited=set()
    while len(visited)<len(G)-1:
        Dmin=inf
        for v in set(G)-visited:
            if D[v]<Dmin:
                Dmin=D[v]
                u=v
        visited.add(u)
        for v,p in G[u]:
            if D[u]+p < D[v]:
                D[v]=D[u]+p
    return D

def Dijkstra(G, U):
    D = {S:inf for S in G}; D[U] = 0
    src = {S: U for S in G}
    visited = set()

    while len(visited) < len(G)-1: # Tant qu'il y des sommets non traités:
        # 1- chercher le sommet V de distance min qui n'est pas encore traité
        Dmin = inf
        for X in set(G)-visited:
        #%#for X in set(G):
            if D[X] < Dmin:
                Dmin = D[X]
                S = X
        #2- Marquer S comme traité
        visited.add(S)
        #3- Mettre à jour des distances des sommets voisins de V (relaxation )
        for V, p in G[S]:
            if D[S] + p < D[V]:
                D[V] = D[S] + p
                src[V] = S
    return D, src
#=.=.=.=.=.=.=.=.=.
    #if X not in visited and D[X] < Dmin:

def shortestPath(G, U, V):
    D, src = Dijkstra(G, U)
    if D[V]== inf: return []
    Path = [V]
    while V != U:
        V = src[V]
        Path[0:0] = [V] #<=> Path.insert(0, V)
    return Path

#=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=
D, src = Dijkstra(G, 'b')
print(D) ; print(src)

Path = shortestPath(G, 'b', 'f')
print(*Path, sep=' ===> ')
# b ===> d ==> e ==> h ==> g ==> f

#############################################################################

D=dijkstra(G,'b')
print(D)
