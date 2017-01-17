# -*- coding: utf-8 -*-
"""Author: Rick Sam
   Comments: Still practicing
   Date: Oct 3, 2016
   """

def traverse(G, s, qtype=set):
    S, Q = set(), qtype()
    Q.add(s)
    while Q:
        u = Q.pop()
        if u in S:
            continue
        S.add(u)
        for v in G[u]:
            Q.add(v)
        yield u

def rec_dfs(G, s, S=None)
    if S is None:
        S = set()
        S.add(s)
        for u in G[s]:
            if u in S:
                continue
            rec_dfs(G, u, S)
