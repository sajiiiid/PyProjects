G = {'a': [ ('d', 2) ],
'b': [ ('c', 5), ('d', 6) ],
'c': [ ('b', 5), ('e', 8) ],
'd': [ ('a', 2), ('b', 6), ('e', 1), ('g', 9), ('h', 6) ],
'e': [ ('c', 8), ('d', 1), ('h', 4) ],
'f': [ ('g', 3) ],
'g': [ ('d', 9), ('f', 3), ('h', 2) ],
'h': [ ('d', 6), ('e', 4), ('g', 2) ]
}
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
names=[ "a", "b", "c", "d", "e", 'f', 'g', 'h' ] ; inf = float('inf')
M = [[inf, inf, inf, 2, inf, inf, inf, inf],
[inf, inf, 5, 6, inf, inf, inf, inf],
[inf, 5, inf, inf, 8, inf, inf, inf],
[2, 6, inf, inf, 1, inf, 9, 6],
[inf, inf, 8, 1, inf, inf, inf, 4],
[inf, inf, inf, inf, inf, inf, 3, inf],
[inf, inf, inf, 9, inf, 3, inf, 2],
[inf, inf, inf, 6, 4, inf, 2, inf]]
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def lstAretes1( M ):
    L = set()
    for i in range( len(M) ): # pour chaque sommet i dans G
        for j in range( len(M[i]) ): # pour chaque j voisin de i
            if M[i][j] not in (0, inf) and (j, i, M[i][j]) not in L:
                L.add( (i, j, M[i][j]) )
    return L
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def lstAretes ( G ):
    L = set()
    for u in G: # pour chaque sommet dans G
        for v,p in G[u]: # pour chaque voisin de u
         if (v, u, p) not in L:
            L.add( (u, v, p) )
    return L
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def union( e, grp, rank ):
    u, v, p = e
    if grp[u] == grp[v] : return
    ##if rank[ grp[u] ] > rank[ grp[v] ]: A, B = u, v
    ##else
    A, B = (u, v) if rank[ grp[v] ] < rank[ grp[u] ] else (v, u)
    gA = grp[A] ; gB = grp[B]
    for s in grp:
        if grp[s] == gB: grp[s] = gA
    rank[gA] += rank[gB]
    return rank[gA]
#=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.
def kruskal( G ):
    grp = { v:v for v in G} # crée les groupements
    rank={u:1 for u in G}   # nbr de sommets ds chaque grpement (initialement ls sommets isolés)
    lst = lstAretes( G )    # créer liste des arretes ordonnée
    lst = sorted(lst, key=lambda x:x[2]) # Triéer dans l'ordre croissant des pondérations
    S = set( ) # ensemble des arretes de l'arbre couvrant minimum (MST)
    for e in lst:
        u, v, p = e
        if grp[u] != grp[v]:
            N = union(e, grp, rank)
            S.add( e )
            if N == len(G): break
    return S
#=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.
def voisin_proche( L, visited ):
    F = set()
    for u, v, p in L: # Construire la liste des voisin de l'acm
        if u in visited and v not in visited: F.add( (u, v, p) )
        elif v in visited and u not in visited: F.add( (v, u, p) )
    return min(F, key=lambda x:x[2] ) # retourner l'arrête reliant le vpp à l'acm
#--------------------------------------------------------------------------------
def Prim( G ):
    L = lstAretes ( G ) ; e = min( L, key=lambda x:x[2] ) # comencer avec l'arrete de poid min
    acm = { e } ; visited = { e[0], e[1] }                # visited contient les sommets de l'acm
    while len(visited) < len(G):         # Tant que l'acm ne contient pas tt ls sommets de G
        vpp = voisin_proche( L, visited )# chercher le voisin le plus proche
        acm.add( vpp )                   # l'ajouter à l'arbre de couverture minimum
        visited.add( vpp[0] ) ; visited.add( vpp[1] )# MAJ des sommets de l'acm
    return acm
#=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.
##E = lstAretes ( G ) ; print(*E, sep='\t', end= '\n'*3)
##E = lstAretes1 ( M ) ; print(*E, sep='\t', end= '\n'*3)
##L = sorted( E, key=lambda x:x[2] ) ; print(*L, sep='\t')
acm1 = kruskal( G ) ; print(*acm1, sep="\t", end='\n'*2)
acm2 = Prim( G ) ; print(*acm2, sep="\t")