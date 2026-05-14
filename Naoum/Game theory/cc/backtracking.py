#=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~

                                                #=~=~=~=~BackTracking=~=~=~=~

#=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
from time import time  ;  from random import *
#=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
def isEnd(s):
    return s==N
#=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
def Cost(s,j):
    return M[s][j]
#=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
def Actions(s):  return set(range(s+1,N+1))
#=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
def Succ(s,a): return a
#=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
def backtrackingSearch(s,visited=None):
    if visited is None: visited = set()
    if isEnd(s): return Cost(s,s), [s]
    visited.add(s)
    minCost, minPath = float('inf'), []
    for a in Actions(s):
        nextS=Succ(s,a)
        if nextS not in visited:
            curCost,curpath=backtrackingSearch(nextS,visited)
            newCost=Cost(s,a)+curCost
            if newCost<minCost:
                minCost=newCost
                minPath=[a]+curpath
    visited.remove(s)
    return minCost, minPath
#=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
def DinamicbacktrackingSearch(s,visited=None):
    if s in cach: return cach[s]
    minCost, minPath = float('inf'), []
    for a in Actions(s):
        nextS=Succ(s,a)
        curCost,curpath=backtrackingSearch(nextS,visited)
        newCost=Cost(s,a)+curCost
        if newCost<minCost:
            minCost=newCost
            minPath=[a]+curpath
    cach[s] = (minCost, minPath)
    return minCost, minPath
#=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
seed(2026)
S0=1 ; N=int(input("?N: "))   ;   inf = float('inf')   ;   cach={N:(0,[])}
M=[[randint(1,2*N)if j>i else inf for j in range(N+1)] for i in range(N+1)]
#=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
t1=time()  ;  sol=backtrackingSearch(S0)  ;  t2=time()  ;  print("Backtracking: ",sol," in ",t2-t1," seconds")

