from time import time

# The order is: [F, W, G, C]
# 0 means the object is on the left side
# 1 means the object is on the right side

S0 = (0, 0, 0, 0)        # everything starts on the left side
GOAL = (1, 1, 1, 1)      # we want everything on the right side

# ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
def IsEnd(s):
   # check if we reached the final state
   return s == GOAL

# ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
def Cost(s, a):
   # every move has the same cost 1
   return 1

# ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
def Actions(s):
   # if the state is bad
   if (s[0] != s[2] and s[2] in (s[1], s[3])):
      return []

   E = [i for i in range(len(s)) if s[i] == s[0]]

   # action is always farmer + something else
   # if x = 0 then farmer goes alone
   return [set([0, x]) for x in E]

# ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
def Succ(s, a):
   # the next state after doing action a
   return tuple([1 - s[i] if i in a else s[i] for i in range(len(s))])

# ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
def backtrackingSearch(s, visited=None):
   if IsEnd(s):
      return 0, []
   if visited == None:
      visited = set()
   if s in visited:
      return float('inf'), []

   visited.add(s)
   minCost, minPath = float('inf'), []

   for a in Actions(s):
      nextS = Succ(s, a)
      curCost, curPath = backtrackingSearch(nextS, visited)
      newCost = curCost + Cost(s, a)
      if newCost < minCost:
         minCost = newCost
         minPath = [a] + curPath
   return minCost, minPath

# ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
def DepthFirstSearch(s, visited=None):
   if IsEnd(s):
      return 0, []
   if visited == None:
      visited = set()
   if s in visited:
      return float('inf'), []
   visited.add(s)

   for a in Actions(s):
      nextState = Succ(s, a)
      curCost, curPath = DepthFirstSearch(nextState, visited)
      if len(curPath) > 0 or IsEnd(nextState):
         newCost = curCost + Cost(s, a)
         return newCost, [a] + curPath
   return float('inf'), []

# ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
def BreadthFirstSearch(s):
   if IsEnd(s):
      return 0, []

   Q = [[s, []]]
   visited = set()

   while Q:
      # pop first element
      curNd, path = Q.pop(0)
      visited.add(curNd)

      # generate all possible moves from current state
      for a in Actions(curNd):
         nextNd = Succ(curNd, a)
         newPath = path + [a]

         # if next state is goal, return result
         if IsEnd(nextNd):
            return len(newPath), newPath

         # check if nextNd is already in the queue
         inQ = False
         for x in Q:
            if x[0] == nextNd:
               inQ = True

         # do not add visited states
         if nextNd in visited or inQ:
            continue

         Q.append([nextNd, newPath])

   return float('inf'), []

# ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
# UCS
# ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
def UniformCostSearch(s):
   Q = [(0, s, [])]
   visited = set()

   while Q:
      # sort by cost
      Q.sort()
      cost, curNd, path = Q.pop(0)
      if IsEnd(curNd):
         return cost, path
      if curNd in visited:
         continue

      visited.add(curNd)

      for a in Actions(curNd):
         nextNd = Succ(curNd, a)
         if nextNd not in visited:
            newCost = cost + Cost(curNd, a)
            newPath = path + [a]
            Q.append((newCost, nextNd, newPath))

   return float('inf'), []

# ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
# A*
# ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
def h(s):
   n = 0
   for x in s:
      if x == 0:
         n += 1
   return n

def A_star(s):
   Q = [(h(s), 0, s, [])]
   visited = set()

   while Q:
      # sort by f value, so best estimated path is first
      Q.sort()
      f, cost, curNd, path = Q.pop(0)
      if IsEnd(curNd):
         return cost, path
      if curNd in visited:
         continue
      visited.add(curNd)

      for a in Actions(curNd):
         nextNd = Succ(curNd, a)
         if nextNd not in visited:
            newCost = cost + Cost(curNd, a)
            newPath = path + [a]
            # f = g + h g is the real cost and h is the heuristic
            newF = newCost + h(nextNd)
            Q.append((newF, newCost, nextNd, newPath))
   return float('inf'), []


# ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
# Affichage:
# ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.

t1 = time(); sol = backtrackingSearch(S0); t2 = time()
print("BT :", sol, f"found in {t2 - t1}s")

t1 = time(); sol = BreadthFirstSearch(S0); t2 = time()
print("BFS:", sol, f"found in {t2 - t1}s")

t1 = time(); sol = DepthFirstSearch(S0); t2 = time()
print("DFS:", sol, f"found in {t2 - t1}s")

t1 = time(); sol = UniformCostSearch(S0); t2 = time()
print("UCS:", sol, f"found in {t2 - t1}s")

t1 = time(); sol = A_star(S0); t2 = time()
print("A* :", sol, f"found in {t2 - t1}s")

# ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
# result:
# ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
'''

BT : (7, [{0, 2}, {0}, {0, 1}, {0, 2}, {0, 3}, {0}, {0, 2}]) found in 0.0001289844512939453s
BFS: (7, [{0, 2}, {0}, {0, 1}, {0, 2}, {0, 3}, {0}, {0, 2}]) found in 9.441375732421875e-05s
DFS: (7, [{0, 2}, {0}, {0, 1}, {0, 2}, {0, 3}, {0}, {0, 2}]) found in 5.555152893066406e-05s
UCS: (7, [{0, 2}, {0}, {0, 3}, {0, 2}, {0, 1}, {0}, {0, 2}]) found in 6.175041198730469e-05s
A* : (7, [{0, 2}, {0}, {0, 3}, {0, 2}, {0, 1}, {0}, {0, 2}]) found in 6.0558319091796875e-05s

'''
####################################################################################################
## EX : 2
####################################################################################################

inf = float('inf')

def minmax(position, depth, alpha, beta, maximizingPlayer):
    # Handle leaf nodes (integers)
    if isinstance(position, int) or depth == 0:
        return position, [position]

    if maximizingPlayer:
        maxEval = -inf
        bestPath = []
        for child in position:
            val, path = minmax(child, depth - 1, alpha, beta, False)
            if val > maxEval:
                maxEval = val
                bestPath = [position] + path
            alpha = max(alpha, val)
            if beta <= alpha:
                break
        return maxEval, bestPath

    else:
        minEval = inf
        bestPath = []
        for child in position:
            val, path = minmax(child, depth - 1, alpha, beta, True)
            if val < minEval:
                minEval = val
                bestPath = [position] + path
            beta = min(beta, val)
            if beta <= alpha:
                break
        return minEval, bestPath

tree = [
    6,
    [3,
        [5, [5, [5], [6]], [4, [7], [4], [5]]],
        [3, [3, [3]]]
    ],
    [6,
        [6, [6, [6]], [6, [6], [9]]],
        [7, [7, [7]]]
    ],
    [5,
        [5, [5, [5]]],
        [8, [8, [9], [8]], [6, [6]]]
    ]
]

depth = 5
eval, path = minmax(tree, depth, -inf, inf, True)

print(f"Winning Value: {eval}")
print(f"Winning Strategy Path: {path}")


# ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
# result:
# ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
'''

Final winning Value: 6
Winning Strategy Path: [[6, [3, [5, [5, [5], [6]], [4, [7], [4], [5]]], [3, [3, [3]]]], [6, [6, [6, [6]], [6, [6], [9]]], [7, [7, [7]]]], [5, [5, [5, [5]]], [8, [8, [9], [8]], [6, [6]]]]], 6]

'''