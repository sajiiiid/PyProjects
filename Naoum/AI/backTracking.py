import numpy as np
from random import *
inf = float('inf')
N=int(input("N?: "))
M=[[randint(1,2*N) if j>i else float('inf') for j in range(N+1)]for i in range(N+1)]
cash={N:(0,[])}

def IsEnd(s): return s == N
def Cost(s,a): return M[s][a]
def Succ(s,a): return a
def Actions(s): return set(range(s+1,N+1))

def backtracking(s,visited=None):
    if IsEnd(s) : return 0, []
    if visited == None : visited=set()
    if s in visited : return inf,[]
    for a in Actions(s):
        nextS = Succ(s,a)
        curCost, curPath = backtracking(nextS,visited)
        newcost = curCost+Cost(s,a)
        if newcost<mincost:
            mincost=newcost
            minPath=[a]+curPath
    return mincost,minPath