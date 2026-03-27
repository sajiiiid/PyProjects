# representation d'un graphe par des listes d'adjasences:
#=. Representation d'un graphe avec un dictionnaire
#Les clés sont les sommet du graphe
#La valeur de chaque clé Vest la liste des successeurs Ui de V
#Clé: valeur <=> V: [(UO, p0), ..(Un, pn)]

G = {
    # Sommet de départ: [liste des sommets d'arriviés avec leurs poids]
    'a': [ ('d', 2)],
    'b': [ ('c', 5), ('d', 6) ],
    'c': [ ('b', 5), ('e', 8) ] ,
    'd': [ ('a' , 2), ('b', 6) , ('e', 1), ('g', 9), ('h', 6) ],
    'e': [ ('c', 8), ('d', 1), ('h', 4) ],
    'f': [('g', 3) ],
    'g': [ ('d', 9), ('f', 3), ('h', 2) ],
    'h': [ ('d', 6), ('e', 4), ('g', 2) ]
}

# representation d'un graphe par une matrice d'adjasences:

inf = float('inf')
Sommets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
N = len(Sommets)

def nbrArretes(M): # graphe non orienté
    nbr = 0
    for i in range(len(M)):
        for j in range(i):
            if M[i][j] not in (0, inf):
                nbr += 1
    return nbr

def nbrArretesOriented(M): # graphe orienté
    nbr = 0
    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[i][j] not in (0, inf):
                nbr += 1
    return nbr

def maxDegre(M): # graphe non orienté
    MaxD = 0; U = 0
    for i in range(len(M)):
        d = 0
        for j in range(len(M)):
            if M[i][j] not in (0, inf): d += 1
        if d > MaxD:
            MaxD = d; U = i
    return MaxD, Sommets[U]

def maxDegreOriented(M): # graphe orienté
    MaxD = 0; U = 0
    for i in range(len(M)):
        d = 0
        for j in range(len(M)): # calculer d+
            if M[i][j] not in (0, inf): d += 1
        for j in range(len(M)): # calculer d-
            if M[j][i] not in (0, inf): d += 1
        if d > MaxD:
            MaxD = d; U = i
    return MaxD, Sommets[U]

def DFS(M, U, visited): # parcour par profondeur d'un graphe à partir d'un sommet U
    if U >= len(M) or U in visited: return
    print(Sommets[U], end=' ')
    visited.append(U)
    for V in range(len(M)):
        if M[U][V] not in (0, inf) and V not in visited:
            DFS(M, V, visited)

def BFS(M, U): # parcour par largeur d'un graphe à partir d'un sommet U
    visited = []
    queue = [U]
    visited.append(U)
    while queue:
        node = queue.pop(0)
        print(Sommets[node], end=' ')
        for V in range(len(M)):
            if M[node][V] not in (0, inf) and V not in visited:
                visited.append(V)
                queue.append(V)

def DFSDict(G, U, visited): # Parcour / profondeur d'un graphe (dict) à partir d'un sommet U
    if U not in G or U in visited: return
    print(U, end=' ')
    visited.append(U)
    for S, p in G[U]:
        if S not in visited:
            DFSDict(G, S, visited)

M = [ [inf if i != j else 0 for j in range(N)] for i in range(N)]
M[0][3] = M[3][0] = 2 #a
M[1][2] = M[2][1] = 5; M[1][3] = M[3][1] = 6 #b
M[2][4] = M[4][2] = 8 #c
M[3][4] = M[4][3] = 1; M[3][6] = M[6][3] = 9; M[3][7] = M[7][3] = 6 #d
M[4][7] = M[7][4] = 4 #e
M[5][6] = M[6][5] = 3 #f
M[6][7] = M[7][6] = 2

print("DFS:"); DFS(M, 7, []) #h, d, a, b, c, e, g, f,
print("\nBFS:"); BFS(M, 4) #e, c, d, h, b, a, g, f,

###=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.=

def nbrArretesG(G): # cas d'un graphe non orienté (dict)
    nbr = 0
    for k in G:
        nbr += len(G[k])
    return nbr // 2

def maxDegreG(G): # cas d'un graphe non orienté (dict)
    maxD, U = 0, None
    for k in G:
        if len(G[k]) > maxD:
            maxD = len(G[k]); U = k
    return maxD, U

def maxDegreGOriented(G): # cas d'un graphe orienté (dict)
    maxD, U = 0, None
    for k in G:
        d = len(G[k]) # calculer d+ de k
        for s in G: # calculer d- de k
            for v, p in G[s]:
                if v == k: d += 1; break
        if d > maxD:
            maxD = d; U = k
    return maxD, U