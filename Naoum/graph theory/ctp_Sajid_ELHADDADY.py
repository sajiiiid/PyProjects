inf = float('inf')
#################################################################
##################### QUESTION 1: ###############################
#################################################################

###Q1 :
#a
M = [
     [inf, 1, inf, inf, 5, 4  , inf, inf, inf, inf, 7  , 9  ],
     [1, inf, 2, inf, inf, inf, 5  , inf, inf, inf, 8  , inf],
     [inf, 2, inf, 3, inf, inf, inf, 2  , inf, inf, inf, inf],
     [inf, inf, 3, inf, 4  , inf, inf, inf, 1, inf, inf, inf],
     [5, inf, inf, 4  , inf, inf, inf, inf, inf, 5, inf, 8  ],
     [4, inf, inf, inf, inf, inf, 6  , inf, inf, 1, inf, inf],
     [inf, 5, inf, inf, inf, 6, inf, 4  , inf, inf, inf, inf],
     [inf, inf, 2, inf, inf, inf, 4, inf, 4  , inf, inf, inf],
     [inf, inf, inf, 1, inf, inf, inf, 4, inf, 2  , inf, inf],
     [inf, inf, inf, inf, 5, 1, inf, inf, 2  , inf, inf, inf],
     [7, 8, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf],
     [9, inf, inf, inf, 8, inf, inf, inf, inf, inf, inf, inf]
    ]
#b
G ={1: [(2, 1), (5, 5), (6, 4), (11, 7), (12, 9)],
    2: [(1, 1), (11, 8), (3, 2), (7, 5)],
    3: [(2, 2), (8, 2), (4, 3)],
    4: [(3, 3), (5, 4), (9, 1)],
    5: [(1, 5), (4, 4), (12, 8), (10, 5)],
    6: [(1, 4), (7, 6), (10, 1)],
    7: [(2, 5), (6, 6), (8, 4)],
    8: [(3, 2), (7, 4), (9, 4)],
    9: [(4, 1), (8, 4), (10, 2)],
    10: [(5, 5), (9, 2), (6, 1)],
    11: [(1, 7), (2, 8)],
    12: [(1, 9), (5, 8)],
    }
#c
L = [(1, 2, 1), (1, 5, 5), (1, 6, 4), (1, 11, 7), (1, 12, 9), (11, 2, 8),
     (2, 3, 2), (2, 7, 5), (3, 8, 2), (3, 4, 3), (4, 5, 4), (4, 9, 1),
     (5, 12, 8), (5, 10, 5),(6, 7, 6), (7, 8, 4),(8, 9, 4), (9, 10 ,2), (10, 6, 1)]

###Q2 :
def lst2Dict(E):
    G = {}
    for U, V, p in E:
        if U not in G: G[U] = []
        if V not in G: G[V] = []
        G[U].append((V, p))
        G[V].append((U, p))  # Add reverse for undirected
    return G

def list2Mat(L):
    Sommets = set()
    for U, V, p in L: Sommets.add(U); Sommets.add(V)
    names = sorted(list(Sommets))   ; N = len(names)
    indice = {names[i]: i for i in range(N)}
    M = [[inf for j in range(N)] for i in range(N)]
    for U, V, p in L:
        i, j = indice[U], indice[V]
        M[i][j] = M[j][i] = p
    return M, names


#################################################################
##################### QUESTION 2 : ##############################
#################################################################

#Q1:
def DFS(G, u, visited = None):
    if visited is None: visited = set()
    if u not in visited:
        print(u, end=', ')
        visited.add(u)
        for v, p in G[u]:
                DFS(G, v, visited)

def BFS(G, U):
    F = [U]
    visited = {U}
    while F:
        S = F.pop(0)
        print(S, end=', ')
        for V, p in G[S]:
            if V not in visited:
                visited.add(V)
                F.append(V)

#Q2 :
def diff_between_BFS_et_DFS(G, U, visited = None):
    DFS(G, U, visited)
    BFS(G, U)

#Q3 :
DFS(G, 1, visited= None)
BFS(G, 1)
diff_between_BFS_et_DFS(G, 1, visited= None)


#################################################################
##################### QUESTION 3 : ##############################
#################################################################



#################################################################
##################### QUESTION 4 : ##############################
#################################################################

#Q1 :
def Dijekstra(G, u):
    D = {v : inf for v in G}
    src = {v : None for v in G}
    D[u] = 0 ; unvisited=list(G.keys())
    while unvisited:
        d_min = inf
        u = None
        for v in unvisited:
            if D[v] < d_min:
                d_min = D[v]
                u = v
        unvisited.remove(u)

        for v, p in G[u]:
            if D[u] + p < D[v]:
                D[v] = D[u] + p
                src[v] = u

    return D, src

#Q2 :
##helper
def edge(G, u, v):
    for s, w in G[u] :
        if s == v:
            return w

def chemin_court(G, u, v):
    D , src = Dijekstra(G, u)
    s = src[v]
    print("(", v, ")"," --",edge(G, s, v) ,"-->","(", s, ")"," --",edge(G, s, src[s]) , "-->", end="")
    while s != u:
        s = src[s]
        if s == u :
            print("(", s, ")")
        else :
            print("(", s, ")", " --",edge(G, s, src[s]) ,"-->", end="")

#exucution
print(Dijekstra(G, 1))
chemin_court(G, 1, 9)