# State Space Search : Tree Search
#==========================================================================================================================================
def isEnd( S ):
    return S == n
#==========================================================================================================================================
def isBad( S ):
    return not(1 <= S <= n)
#==========================================================================================================================================
def Actions( S ):
    f = lambda x: x+1
    g = lambda x: 2*x
    return [(1, f), (2, g)]
#==========================================================================================================================================
def Succ( S, a ):
    cost, h = a
    return h( S )
#==========================================================================================================================================
def Cost( S, a ):
    return a[0]
#==========================================================================================================================================
def backtrackingSearch( s ):
    #if s in visited: return (float('inf'), [])
    if isEnd(s): return (0, [s])
    if isBad(s): return (float('inf'), [])
    
    visited.append( s )
    bestCost, minPath = float('inf'), [ ]
    for a in Actions(s):
        S1 = Succ(s, a)
        curCost, curPath = backtrackingSearch( S1 )
        newCost = Cost(s, a) + curCost
        #print( s, S1, newCost)
        
        if newCost < bestCost:
            bestCost = newCost
            minPath = [s]+curPath
    
    return bestCost, minPath
#=============================================================================================================================
def DFS( s ):
    if isEnd(s): return [s]
    if isBad(s): return [ ]
    
    visited.append( s )
    bestCost, minPath = float('inf'), [ ]
    for a in Actions(s):
        S1 = Succ(s, a)
        curPath = DFS( S1 )
        
        if curPath: return [s]+curPath
    return [ ]
#============================================================================================================================
def newDFS( s, maxD=10, d=0 ):
    if d > maxD: return [ ]
    if isEnd(s): return [s]
    if isBad(s): return [ ]
    
    visited.append( s )
    bestCost, minPath = float('inf'), [ ]
    for a in Actions(s):
        S1 = Succ(s, a)
        curPath = newDFS( S1, maxD, d+1 )
        
        if curPath: return [s]+curPath
    return [ ]
#===================================================================================================================================
def DFS_ID(s):
    for d in range(1, 20):
        sol = newDFS(s, maxD= d)
        if sol: return sol
    return [ ]

S_start = 1
n = 20
visited = []
Sol = backtrackingSearch( S_start )
print("BT: ", Sol[0]) ; print(*Sol[1], sep='--->' )

Sol = DFS( S_start )
print("DFS: "); print(*Sol, sep='--->' )

Sol = DFS_ID( S_start )
print("DFS_ID: "); print(*Sol, sep='--->' )