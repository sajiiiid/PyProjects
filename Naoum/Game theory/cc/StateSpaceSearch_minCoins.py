def IsEnd( s ):
   return s == 0 # <=> s in coinLst

def Cost(s, a): 
   return 1

def Actions(s):
   E = [ ]                           # set();
   for coin in coinLst:
      if s-coin >= 0: 
         E.append(coin) # E.add(coin)
   return E

def Succ(s, a): 
   return s-a

def backtrackingSearch( s ):
   if IsEnd(s): return 0, [s]
   minCost, minPath = float('inf'), []
   for a in Actions(s):
      curCost, curPath = backtrackingSearch( Succ(s, a) )
      newCost = curCost + Cost(s, a)
      if newCost < minCost:
         minCost = newCost
         minPath = [a] + curPath      
   return minCost, minPath

def DepthFirstSearch( s ):
   if IsEnd(s): return 0, [s]
   for a in Actions(s):
      curCost, curPath = DepthFirstSearch( Succ(s, a) )
      if len(curPath) > 0:
         newCost = curCost + Cost(s, a)
         return newCost, [a]+curPath
   return float('inf'), []

def BreadthFirstSearch( s ):
   if IsEnd(s): return 0, [s]
   Q = [ [s, [ ]]  ] # FIFO
   visited = set()
   while Q:
      curNd, path = Q.pop( 0 )   # retrive the First unprocessed state
      visited.add( curNd ) # mark as visited! do not visit later

      for a in Actions( curNd ):# expolore each child of current state
         nextNd = Succ(curNd, a)# if it's a solution ==> return the path
         newPath = path+[a]
         if IsEnd( nextNd ): return len(newPath), newPath
         if nextNd in visited or nextNd in Q:
            continue #ignore if alredy explored
         Q.append([nextNd, newPath])# Add to Queue as a base of new exploration
   return float('inf'), []

from time import time
S0 = 348 ; coinLst = [200, 100, 50, 20, 10, 5, 2, 1]

t1 = time() ; sol = BreadthFirstSearch( S0 ) ; t2 = time()
print("BFS:", sol, f"found in {t2-t1}s")

t1 = time() ; sol = DepthFirstSearch( S0 ) ; t2 = time()
print("DFS:", sol, f"found in {t2-t1}s")

t1 = time() ; sol = backtrackingSearch( S0 ) ; t2 = time()
print('BT:', sol, f"found in {t2-t1}s")
