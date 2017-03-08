#!/usr/bin/python
#Pattern matching

class PatMatch:
    def __init__(self):
        self.patterns = []
        self.working = [0] * 50
        self.worktop = 0
        self.nMatches = 0

    def addPattern(self, pattern, callBack):
        self.patterns.append((pattern, len(pattern), callBack))

    def reset(self):
        self.worktop = 0
        self.nMatches = 0

    def seeChar(self, ch):
        for p in self.patterns:
            if ch == p[0][0]
                self.working[self.worktop] = [p, 0]
                self.worktop += 1

        wp = wk = 0
        while wp <self.worktop:
            wpat, wcp = self.working[wp]
            if wpat[0][wcp] == ch:
                wcp += 1
            if wcp >= wpat[1]:
                wpat[2](wpat[0])
                self.nMatches += 1
            else:
                self.working[wk] = (wpat, wcp)
                wk  += 1
        wp += 1
        self.worktop = wk
