"""
Author: Rick Sam
Date: Oct 3
Comments: Tree
"""

def walk(G, s, S=set()): #Walk the graph from node s
    P, Q = dict(), set() # Predecessor + "to do " queue
    P[s] = None #s has no predecssor
    Q.add(s) # start from s
    while Q: # still nodes to visit
        u = Q.pop() #Pick one, arbitarily
        for v in G[u].difference(P,S):
            Q.add(v)
            P[v] = u
    return P
