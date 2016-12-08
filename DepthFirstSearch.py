"""Depth First Search is one of the most important traversal algorithm, Also known as Backtracking"""

def rec_dfs(G, s, S=None):
    if S is None:
        S = set()
    S.add(s)
    for u in G[s]:
        if u in S:
            continue
        rec_dfs(G, u, S)

def traversal(G, s, qtype = set):
    S, Q = set(), qtype()
    Q.add(s)
    while Q:
        u = Q.pop()
        if u in S:
            continue
        s.add(u)
        for v in G[u]:
            Q.add(v)
        yield u

