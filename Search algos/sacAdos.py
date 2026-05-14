from os import stat_result
from random import random, randint; from math import exp, inf


def generate_neighbor(solution):
    bar = lambda  x : x-1
    number = randint(0, 3)
    solution[number] = bar(solution[number])
    return solution

def objective(curr_sol):
    if sum(curr_sol) <= 5 :
        s = 0
        for i in range(len(curr_sol)) :
            s = V[i] * W[i]
        return s
    return -inf

def knapsak_value(solution, wights, values, maxCapasity):
    totalWigth = sum(w * x for w, x in zip(wights, solution))
    totalValue = sum(v * x for v, x in zip(values, solution))
    return totalValue if totalValue <= maxCapasity else - inf



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

W=[2, 3, 4, 5]; V=[3, 4, 5, 6]; maxCapacity = 10; maxIter = 100; temp = 100
coolingRate = 0.95; initialS = [0, 0, 0, 0]

simulated_annealing(objective, initialS, temp, coolingRate)
