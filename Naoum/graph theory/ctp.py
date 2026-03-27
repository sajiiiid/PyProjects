##############################################################################
### PART 1: CONVERSIONS (NON-ORIENTED / UNDIRECTED)
### Source: TD1-graphe_Q12.pdf
##############################################################################

# 1. Dictionary -> Edge List (Set of tuples)
def dict2Lst(G):
    E = set()
    for U in G:
        for V, p in G[U]:
            # Check the reverse edge to avoid duplicates in the undirected graph
            if (V, U, p) not in E:
                E.add((U, V, p))
    return list(E)  # Return list for easier viewing

# 2. Edge List -> Dictionary
def lst2Dict(E):
    G = {}
    for U, V, p in E:
        if U not in G: G[U] = []
        if V not in G: G[V] = []
        G[U].append((V, p))
        G[V].append((U, p))  # Add reverse for undirected
    return G

# 3. Edge List -> Matrix
def list2Mat(L):
    Sommets = set()
    for U, V, p in L: Sommets.add(U); Sommets.add(V)
    names = sorted(list(Sommets))   ; N = len(names)
    # Map name to index: {'a': 0, 'b': 1...}
    indice = {names[i]: i for i in range(N)}
    # Init matrix with inf
    M = [[inf for j in range(N)] for i in range(N)]
    for U, V, p in L:
        i, j = indice[U], indice[V]
        M[i][j] = M[j][i] = p
    return M, names

# 4. Matrix -> Edge List
def mat2Lst(M, names):
    E = set()
    for i in range(len(M)):
        for j in range(i):  # Read only the lower triangle (j < i)
            if M[i][j] != inf:
                U, V, p = (names[i], names[j], M[i][j])
                E.add((U, V, p))
    return list(E)

# 5. Dictionary -> Matrix
def dict2Mat(G):
    names = sorted(G.keys()); N = len(names)
    indice = {names[i]: i for i in range(N)}
    M = [[inf if i != j else 0 for j in range(N)] for i in range(N)]
    for U in G:
        for V, p in G[U]:
            i, j = indice[U], indice[V]
            M[i][j] = M[j][i] = p
    return M, names

# 6. Matrix -> Dictionary
def mat2Dict(M, names):
    G = {name: [] for name in names}
    for i in range(len(M)):
        for j in range(i):  # Read lower triangle
            if M[i][j] != inf:
                U, V, p = (names[i], names[j], M[i][j])
                G[U].append((V, p))
                G[V].append((U, p))  # Add reverse
    return G


##############################################################################
### PART 2: TRAVERSALS (BFS & DFS)
### Source: TD1-graphe_Q12.pdf
##############################################################################

# Depth-First Search (Profondeur) - Recursive
def DFS(G, U, visited=None):
    if visited is None: visited = set()
    if U not in visited:
        print(U, end=" ")
        visited.add(U)
        for V, p in G[U]:
            DFS(G, V, visited)

# Breadth-First Search (Largeur) - Iterative
def BFS(G, U):
    F = [U]  # Queue
    visited = {U}  # Visited Set
    while F:
        S = F.pop(0)  # Dequeue (pop first)
        print(S, end=" ")
        for V, p in G[S]:
            if V not in visited:
                visited.add(V)
                F.append(V)


##############################################################################
### PART 3: MINIMUM SPANNING TREE (MST)
### Source: GISIBA_1_MST.pdf
##############################################################################

# Kruskal's Algorithm (Easiest Implementation)
def kruskal(G):
    # 1. Setup
    grp = {S: S for S in G}  # Each node is its own group initially
    MST = {S: [] for S in G}  # Result tree
    Val = 0  # Total weight
    # 2. Create a sorted edge list
    E = []
    for U in G:
        for V, p in G[U]:
            if (V, U, p) not in E:  # No duplicates
                E.append((U, V, p))
    E.sort(key=lambda x: x[2])  # Sort by weight (p)
    # 3. Process edges
    for U, V, p in E:
        if grp[U] != grp[V]:  # If in different groups
            # Add to MST
            MST[U].append((V, p))
            MST[V].append((U, p))
            Val += p
            # Merge Groups (Naive method: update all nodes in group U)
            old_g = grp[U]
            new_g = grp[V]
            for node in grp:
                if grp[node] == old_g:
                    grp[node] = new_g
    return MST, Val

# Prim's Algorithm (Easiest Implementation)
def Prim(G):
    MST = {S: [] for S in G}
    Val = 0
    covred = set()
    # 1. Find start edge (global minimum)
    min_w = inf
    start_edge = None
    for U in G:
        for V, p in G[U]:
            if p < min_w:
                min_w = p
                start_edge = (U, V, p)
    if start_edge:
        U, V, p = start_edge
        covred.add(U)
        covred.add(V)
        MST[U].append((V, p))
        MST[V].append((U, p))
        Val += p
    # 2. Loop until all covered
    while len(covred) < len(G):
        min_w = inf
        next_edge = None
        # Find the smallest edge between covered and uncovered
        for S in G:
            for V, p in G[S]:
                # Check if the edge crosses the boundary
                if ((S in covred and V not in covred) or
                        (S not in covred and V in covred)):
                    if p < min_w:
                        min_w = p
                        next_edge = (S, V, p)
        if next_edge:
            U, V, p = next_edge
            MST[U].append((V, p)); MST[V].append((U, p))
            covred.add(U)        ; covred.add(V)
            Val += p
        else:
            break  # Graph disconnected

    return MST, Val
##############################################################################
### PART 4: SHORTEST PATH (DIJKSTRA)
### Source: myDisjktra.pdf
##############################################################################

# Version A: Simple (Returns distances only)
def Dijkstra_Simple(G, Start):
    D = {v: inf for v in G}
    D[Start] = 0
    visited = set()
    while len(visited) < len(G):
        # 1. Find unvisited node with min distance
        Dmin = inf
        u = None
        for v in G:
            if v not in visited and D[v] < Dmin:
                Dmin = D[v]
                u = v
        if u is None: break
        visited.add(u)
        # 2. Relax neighbors
        for v, p in G[u]:
            if D[u] + p < D[v]:
                D[v] = D[u] + p
    return D


# Version B: Complete (Returns Predecessors for path reconstruction)
def Dijkstra_Complete(G, Start):
    D = {v: inf for v in G}
    src = {v: None for v in G}  # Predecessors
    D[Start] = 0
    visited = set()
    while len(visited) < len(G):
        Dmin = inf
        u = None
        for v in G:
            if v not in visited and D[v] < Dmin:
                Dmin = D[v]
                u = v
        visited.add(u)

        for v, p in G[u]:
            if D[u] + p < D[v]:
                D[v] = D[u] + p
                src[v] = u  # Save where we came from
    return D, src


##############################################################################
### EXECUTION TEST
##############################################################################
inf = float('inf')
G = {
    'a': [('d', 2)],
    'b': [('c', 5), ('d', 6)],
    'c': [('b', 5), ('e', 8)],
    'd': [('a', 2), ('b', 6), ('e', 1), ('g', 9), ('h', 6)],
    'e': [('c', 8), ('d', 1), ('h', 4)],
    'f': [('g', 3)],
    'g': [('d', 9), ('f', 3), ('h', 2)],
    'h': [('d', 6), ('e', 4), ('g', 2)]
}
for u in G :
    for v, p in G[u]:
        print(v,p)

'''
print("--- TRAVERSALS ---")
BFS(G, 'a')
DFS(G, 'a')
print("\n")

print("--- MST ALGORITHMS ---")
mst_k, val_k = kruskal(G)
print(f"Kruskal Val: {val_k}")
mst_p, val_p = Prim(G)
print(f"Prim Val: {val_p}")
print("\n")

print("--- DIJKSTRA ---")
dists, preds = Dijkstra_Complete(G, 'a')
print(f"Distances from 'a': {dists}")'''