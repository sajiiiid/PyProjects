#=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~

## Simulated Annealing Algorithm for the Knapsack Problem

#=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~

from random import random, randint ; from math import exp

def objective(solution):
    total_weight = 0
    total_value = 0
    for i in range(len(solution)):
        if solution[i] == 1:
            total_weight += poids[i]
            total_value += valeur[i]
    
    if total_weight > capacite:
        return -inf
    return total_value

def generate_neighbor(current_solution):
    neighbor = current_solution.copy()
    index = randint(0, len(neighbor) - 1)
    bar=lambda x: 1-x
    neighbor[index] = bar(neighbor[index])
    return neighbor

def simulated_annealing(objective, x0, temp, cooling_rate):
    current_sol=x0
    current_val=objective(current_sol)
    best_sol=current_sol
    best_val=current_val
    while temp >1:
        neighbor=generate_neighbor(current_sol)
        neighbor_val=objective(neighbor)
        if neighbor_val > current_val or exp((neighbor_val - current_val) / temp) > random():
            current_sol=neighbor
            current_val=neighbor_val
        if current_val > best_val:
            best_sol=current_sol
            best_val=current_val
            print(f"best solution: {best_sol}   |   current solution: {current_sol}")
        temp *= cooling_rate
    return best_sol, best_val
#=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~

#probleme sac a dos 
inf=float('inf')  ;  poids = [2,3,4,5]  ;  valeur = [3,4,5,6]  ;  capacite = 5
sol = [0,0,0,0]   ;  maxIter=100 ;  temp = 100 ;  coolingRate=0.95

#=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~

best_solution, best_value = simulated_annealing(objective, sol, temp, coolingRate)
print("Meilleure solution trouvée:", best_solution)
print("Valeur de la meilleure solution:", best_value)
