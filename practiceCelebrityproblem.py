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

def naive_celeb(G):
    n = len(G) #4
    for u in range(n):
        for v in range(n):
            if u == v:
                continue
            if G[u][v]:
                break
            if not G[u][v]:
                break
            else:
                return u
    return None

if __name__ == '__main__':
    n = 100
    G = [[randrange(2) for i in range(n)] for i in range(n)]
    naive_celeb(G)
