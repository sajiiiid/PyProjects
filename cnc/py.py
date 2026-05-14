import numpy as np
import matplotlib.pyplot as plt

## np.zeros(n, m)
## np.ones(n, m)
## np.eye(n)
## np.arrar( L )

def matrice_zeros(n, m):
    l = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(0)
        l.append(row)
    mat = np.array(l)
    return mat

print(matrice_zeros(3, 8))

def matrice_id(n):
    return np.eye(n)

def sigma(L, U, i, j):
    somme = 0
    for k in range(i):
        somme += L[i][k] * U[k][j]
    return somme

mat1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
mat2 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

multMat = np.dot(mat1, mat2)   #.dot()
maltMat2 = mat1 @ mat2

print(multMat)
print(maltMat2)



