G = {
'a': [ ('d', 2) ],
 'b': [ ('c', 5), ('d', 6) ],
 'c': [ ('b', 5), ('e', 8) ],
 'd': [ ('a', 2), ('b', 6), ('e', 1), ('g', 9), ('h', 6) ],
 'e': [ ('c', 8), ('d', 1), ('h', 4) ],
 'f': [ ('g', 3) ],
 'g': [ ('d', 9), ('f', 3), ('h', 2) ],
 'h': [ ('d', 6), ('e', 4), ('g', 2) ]
 }
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def kruskal(G):
    MST = {S:[] for S in G} ; Val = 0 ; n = len( G ) ; m = 0
    grp = {S: S for S in G} ; covred = set( )
    E = toEdgesLst( G )  ; E = sorted( E, key=lambda x:x[-1] )
    for U, V, p in E:
        if grp[U] != grp[V] :
            addEdge( MST, (U, V, p), covred )
            for S in grp:
                if grp[S] == grp[U]:
                    grp[S] = grp[V]
            Val += p ; m = m + 1
        if m == n-1: break
    return MST, Val
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def getGrp(grp, U):
    V = grp[U]
    if V == U: return U
    S = getGrp(grp, V)
    grp[U] = S
    return S
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def taille(grp, U):
    nbr = 0
    for S in grp:
        if getGrp(grp, S) == getGrp(grp, U): nbr += 1
    return nbr
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def toEdgesLst( G ):
    E = set()
    for S in G:
        for V, p in G[ S ]:
            if (V, S, p) not in E: # Only add the edge if the reverse isn't already there
                E.add( (S, V, p) )
    return E
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def Prim( G ):
    MST = { S:[] for S in G } ; Val = 0 ; covred = set( )
    e_min = findMinimumEdge( G ) # e_min = findNextEdge1( G, covred )
    addEdge( MST, e_min, covred ) ; Val += e_min[-1]
    while len(covred) < len(G):
        NextEdge = findNextEdge(G, covred)
        addEdge( MST, NextEdge, covred ) ; Val += NextEdge[-1]
    return MST, Val
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def addEdge( MST, e, covred):
    U, V, p = e
    MST[U].append( (V, p) )
    MST[V].append( (U, p) )
    covred.add( U )
    covred.add( V )
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def findNextEdge( G, covred):
    minW = float('inf') ; nextEdge = None
    for S in G:
        for V, p in G [S]:
            if p<minW and ((V in covred and S not in covred) or (V not in covred and S in covred)):
                minW = p
                nextEdge = (S, V, p)
    return nextEdge
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def findMinimumEdge( G ):
    minW = float('inf') ; e_min = None
    for S in G:
        for V, p in G [S]:
            if p < minW:
                minW = p
                e_min = (S, V, p)
    return e_min
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def findNextEdge1( G, covred ):
    minW = float('inf') ; nextEdge = None
    for S in G:
        for V, p in G [S]:
            if not covred or((V in covred and S not in covred)or(V not in covred and S in covred)):
                if p < minW:
                    minW = p
                    nextEdge = (S, V, p)
    return nextEdge
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
MST, Val = Prim( G ) ;
print("Prim algo\n",Val, *MST.items(), sep='\n')
print("")
MST, Val = kruskal( G ) ;
print("kruskal algo\n",Val, *MST.items(), sep='\n')