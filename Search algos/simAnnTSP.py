from random import random, randint; from math import exp

def generate_neighbor(solution):
    neighbor = solution[:]

    i = randint(0, len(solution) -1)
    j = randint(0, len(solution) -1)

    solution[i], solution[j] = solution[j], solution[i]

    return solution

def objective(X, D) :
    V= 0
    for k in range(len(X) - 1):
        i, j = X[k], X[k + 1]
        V += D[i][j]
    i, j = X[-1], X[0]
    return V + D[i][j]

def simulated_annealing(objective, x0, temp, cooling_rate):
    curr_sol = x0
    curr_val = objective(curr_sol)
    best_sol = curr_sol
    best_val = curr_sol

    while temp > 1 :
        neighbor = generate_neighbor(curr_sol)
        neighbor_val = objective(neighbor)
        if (neighbor_val - curr_val) or exp((neighbor_val - curr_val)/ temp) > random() :
            curr_sol, curr_val = neighbor, neighbor_val

        if curr_val > best_val :
            best_sol, best_val = curr_sol, curr_val
            temp *= cooling_rate

    return best_sol, best_val

M =[[0,10,15,20], [10,0,35,25], [15,35,0,30], [20,25,30,0]]
maxCapacity = 10; maxIter = 100; temp = 100; coolingRate = 0.95; initialS = [0, 0, 0, 0]

