from time import time
import numpy as np
#~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
#                      Initialization
#~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
def T( s, a, s2 ):
   return P.get( (s,a,s2) , 0)
#~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
def reward( s, a, s2 ): return R.get( (s,a,s2) , 0)
#~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
def printVals(V, name="Pi"):
   print(f"Values of states under policy {name}:")
   for s in V:
      print(s, '-->',f"{V.get((s), -inf): 7.3f}", end= ';\t')
   print()      
#~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.      
def printPolicy(pi):
   print("Policy pi:")
   for s in pi:
      print( s, '-->', pi.get( s, '#'), end= ' \t')
   print()
#~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
# Value iteration
#~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
def valueIteration(EPSILON = 1e-4, maxIter=200, VERBOSE=False ):
   optPolicy = {}
   V = { s:0 for s in S }
   for iteration in range( maxIter ):
      oldV = V.copy()
      maxDiff = 0
      for s in S:
         maxV = -inf
         for a in actions[s]:
            #----------------------------------------------------
            curV = 0
            for s2 in S:
               curV += T(s, a, s2)*( reward(s, a, s2) + GAMMA*oldV[s2])
            #----------------------------------------------------               
            if curV > maxV:
               maxV = curV
   
               optPolicy[s] = a
               
         V[s] = maxV
         maxDiff = max(maxDiff, np.abs(oldV[s] - V[s]))
         
      if maxDiff < EPSILON: break
      if VERBOSE : print(iteration, "*"*50) ; printVals( V )
   return V, optPolicy
#~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
# Policy Evaluation
#~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
def policyEvaluation(Pi, EPSILON = 1e-4, maxIter=200, VERBOSE=False ):
   V = { s:0 for s in S }
   for iteration in range( maxIter ):
      oldV = V.copy()
      maxDiff = 0
      for s in S:
         a = Pi[s]
         curV = 0
         for s2 in S:
            curV += T(s, a, s2)*( reward(s, a, s2) + GAMMA*oldV[s2])
         V[s] = curV
         
         maxDiff = max(maxDiff, np.abs(oldV[s] - V[s]))
         
      if maxDiff < EPSILON: break
      if VERBOSE : print(iteration, "*"*50) ; printVals( V )
   return V
#~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
# Policy Iteration
#~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
def policyIteration(EPSILON = 1e-15, maxIter=200, VERBOSE=False ):
   optPolicy = {}
   #....
   for iteration in range(maxIter) :
      if VERBOSE : print(iteration, "*"*50) ; printVals( V )
   #....
   return V, optPolicy
#~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.      
GAMMA = 0.8   ;  S = set( range(4) ) ; inf = float("inf")

actions = { 0:{'E', 'N'},
            1:{'E', 'N', 'R'},
            2:{'E', 'N', 'R'},
            3:{'R'} }
P = {}
P[(0,'E',0)] = 3/4 ; P[(0,'E',1)] = 1/4  ;  P[(0,'N',1)] = 4/5 ;  P[(0,'N',3)] = 1/5

P[(1,'E',1)] = 4/7 ; P[(1,'E',2)] = 2/7  ;  P[(1,'E',3)] = 1/7
P[(1,'R',0)] = 1
P[(1,'N',2)] = 4/5 ; P[(1,'N',3)] = 1/5

P[(2,'E',2)] = 3/4 ; P[(2,'E',3)] = 1/4
P[(2,'N',2)] = 1/2 ; P[(2,'N',3)] = 1/2
P[(2,'R',0)] = 1

P[(3,'R',0)] = 1

R = {}
R[(0,'E',0)] = R[(0,'E',1)] = 2500  ;  R[(0,'N',1)] = R[(0,'N',3)] = 3000
R[(1,'E',1)] = R[(1,'E',2)] = R[(1,'E',3)] = 500
R[(1,'N',2)] = R[(1,'N',3)] = 1500
R[(1,'R',0)] = -500

R[(2,'E',2)] = R[(2,'E',3)] = -1000
R[(2,'N',2)] = R[(2,'N',3)] = 500
R[(2,'R',0)] = -2500

R[(3,'R',0)] = -3000
#~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
t1 = time()  ;  Vopt, optPolicy = valueIteration( )  ;  t2 = time()
print(t2 - t1)   ; policyR= {0:'E', 1:'N', 2:'E', 3:'R'}
VR = policyEvaluation(policyR)
V  = policyEvaluation(optPolicy)
#~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
print("~."*20); printVals(Vopt, 'Optimal via VI')
print("~."*20); printPolicy(optPolicy)

print("~."*20); printVals(VR, "R")
print("~."*20); printVals(V, "Opt")
