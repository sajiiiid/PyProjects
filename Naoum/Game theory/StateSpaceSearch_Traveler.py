def IsEnd( s ): return s == N
#~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
def Cost(s, j):
   if IsEnd(s): return 0
   if s > j   : return inf
   if not j%s : return j//s
   return j-s
#~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
def Actions(s): return set( range(s+1, N+1) )
#~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
def Succ(s, a): return a
#~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
def DP_travller( s=1 ):
   if s in cach: return cach[s]
   minCost, minPath = inf, []
   for a in Actions(s):
      nextS = Succ(s, a)
      curCost, curPath = DP_travller( nextS )
      newCost = curCost + Cost(s, a)
      if newCost < minCost:
         minCost = newCost
         minPath = [a] + curPath
   cach[s] = (minCost, minPath)
   return cach[s]
#~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
def backtrackingSearch( s, visited=None ):
   if IsEnd(s): return 0, []
   if visited==None: visited = set()
   if s in visited: return inf, []
   
   minCost, minPath = inf, []
   for a in Actions(s):
      nextS = Succ(s, a)
      curCost, curPath = backtrackingSearch( nextS, visited )
      newCost = curCost + Cost(s, a)
      if newCost < minCost:
         minCost = newCost
         minPath = [a] + curPath      
   return minCost, minPath
#~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
from time import time
S0=1 ; N = int(input("?N: ")) ; inf = float('inf') ; cach = {N:(0,[])}
#~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
t1 = time() ; sol = DP_travller( S0 ) ; t2 = time()
print('DP:', sol, f"found in {t2-t1}s")

t1 = time() ; sol = backtrackingSearch( S0 ) ; t2 = time()
print('BT:', sol, f"found in {t2-t1}s")

