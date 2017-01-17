# -*- coding: utf-8 -*-
"""
  Author: Rick Sam
  Date: September 20, 2016
  Comments: Read about Stephen Wolfram, interesting guy. I think, if someone's a real genius, they won't tell anyone
  or show off. People like him, struggle with a lot of pride. And as, John Owen says, we must mortify
  the flesh constantly, not by ourself but by relying on [HIM]. Gosh, I struggle with it a lot.
  What is the greatest thing we can do? To give up ourselves for other people John 15:13
"""
from random import randrange

def celeb(G):
    n = len(G)
    u, v = 0, 1
    for c in range(2, n+1):
        if G[u][v]:
            u=c
        else:
            v = c
    if u ==n:
        c = v
    else:
        c = u
    for v in range(n):
        if c ==v:
            continue
        if G[c][v]:
            break
        if not G[v][c]:
            break
        else:
            return c
        return None

if __name__ == '__main__':
    n = 100
    G = [[randrange(2) for i in range(n)] for i in range(n)]
    print celeb(G)
    print G[1:10]
