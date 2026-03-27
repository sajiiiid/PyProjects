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


def Kruskal_Exam_Version(G):
    grp = {node: node for node in G}
    E = []

    for u in G:
        for v, w in G[u]:
            if u < v:  # Avoid duplicates like (A,B) and (B,A)
                E.append((u, v, w))

    E.sort(key=lambda x: x[2])
    MST = []  # The result list
    Val = 0  # Total weight
    m = 0  # Edge counter
    n = len(G)  # Number of nodes

    for u, v, w in E:
        id_u = grp[u]
        id_v = grp[v]
        if id_u != id_v:
            MST.append((u, v, w))
            Val += w
            for node in grp:
                if grp[node] == id_v:
                    grp[node] = id_u
            if m == n - 1:
                break

    return MST, Val
