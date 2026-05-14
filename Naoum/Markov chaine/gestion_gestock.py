import numpy as np
from time import time

# ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
#                    Initialization
# ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
C_max = 2; N = 2; c = 2; h = 3; v = 6; S = {0, 1, 2}

# Actions possibles pour chaque état (quantité à commander)
actions = {s: list(range(C_max - s + 1)) for s in S}

# Probabilités de demande Q[d][y] (demande d, stock y)
Q = {
    0: {0: 0.4, 1: 0.1, 2: 0.0},
    1: {0: 0.3, 1: 0.4, 2: 0.4},
    2: {0: 0.3, 1: 0.5, 2: 0.6}
}


# ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
def T(s, a, s2):
    """Calcule la probabilité de transition p_ij(a)"""
    y = s + a
    if s2 > 0 and s2 <= y:
        d = y - s2  # Si le stock restant est s2, la demande était de (y - s2)
        return Q[d][y]
    elif s2 == 0:
        # Si le stock tombe à 0, la demande a couvert ou dépassé le stock
        return sum(Q[d].get(y, 0) for d in range(y, N + 1))
    return 0


# ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
def expected_cost(s, a):
    """Calcule le coût immédiat espéré (Achat + Stockage - Revenu)"""
    y = s + a
    cost_a = c * a
    exp_stock_rev = 0
    for d in range(N + 1):
        stock_cost = h * max(0, y - d)
        revenue = v * min(d, y)
        exp_stock_rev += Q[d][y] * (stock_cost - revenue)
    return cost_a + exp_stock_rev


# ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
def printVals(V, g):
    print(f"Gain moyen (g): {g:.2f}")
    for s in sorted(S):
        print(f"V({s}) = {V[s]:.2f}", end='\t')
    print()


# ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
def printPolicy(optPolicy):
    print("Politique (Stock Initial -> Quantité à commander):")
    for s in sorted(S):
        print(f"S={s} -> Cder {optPolicy[s]}", end='\t')
    print()


# ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
# Policy iteration (Algorithme de Howard)
# ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
def policyIteration(maxIter=200, VERBOSE=False):
    # Initialisation : on choisit de commander le maximum possible
    optPolicy = {s: max(actions[s]) for s in S}
    V = {s: 0 for s in S}
    g = 0

    for iteration in range(maxIter):

        # 1. Évaluation de la politique (Résolution du système d'équations)
        A = np.zeros((len(S), len(S)))
        B = np.zeros(len(S))

        for i in S:
            a = optPolicy[i]
            if i < C_max: A[i, i] += 1
            for j in range(C_max):
                A[i, j] -= T(i, a, j)
            A[i, C_max] = 1  # Colonne pour la variable 'g'
            B[i] = expected_cost(i, a)

        x = np.linalg.solve(A, B)
        for i in range(C_max): V[i] = x[i]
        V[C_max] = 0  # Par convention, on fixe V(C_max) à 0
        g = x[C_max]

        if VERBOSE:
            print(iteration, "*" * 50)
            printVals(V, g)

        # 2. Amélioration de la politique
        policy_stable = True
        for s in S:
            old_action = optPolicy[s]
            min_q = float('inf')

            for a in actions[s]:
                # On cherche l'action qui minimise Q(s,a) = Cost(s,a) + Somme( P * V )
                q_val = expected_cost(s, a) + sum(T(s, a, s2) * V[s2] for s2 in S)
                if q_val < min_q - 1e-9:  # Tolérance pour les calculs flottants
                    min_q = q_val
                    optPolicy[s] = a

            if old_action != optPolicy[s]:
                policy_stable = False

        if policy_stable:
            break

    return V, optPolicy, g


# ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
t1 = time();
V, optPolicy, g = policyIteration(VERBOSE=True);
t2 = time()
print(f"Temps d'exécution : {t2 - t1:.5f}s")
# ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
print("~." * 20);
printVals(V, g)
print("~." * 20);
printPolicy(optPolicy)