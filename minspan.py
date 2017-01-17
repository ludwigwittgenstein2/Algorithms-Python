import random, sys, sarg
from   pgcon import Pgcon, WHITE, RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, TURQUO

colors = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, TURQUO)

class Minnode :
    def __init__ (self, pos, label, group) :
        self.pos = pos
        self.label = label
        self.group = group

    def __str__ (self) :
        return "<%s at %s in group %d>" % (self.label, self.pos, self.group)

    __repr__ = __str__

class Minspan :
    def __init__ (self, pgcon, pixels, nNodes) :
        letters    = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.pgcon   = pgcon            # pgame interface
        self.nodes = [Minnode(randpos(20,pixels-20), letters[i], i+1)
                                    for i in range(nNodes)]
        self.plinks = []          # potential links between nodes
        self.pixels = pixels
        for m in range(nNodes) :
            for n in range(m+1,nNodes) :
                x = self.nodes[m]
                y = self.nodes[n]
                dist = euclDist2(x.pos,y.pos)
                self.plinks.append((dist,x,y))
        self.plinks.sort()
        self.links = []

    def linkNodes (self) :
        nLinks = 0
        while self.plinks :
            plink = self.plinks.pop(0)
            dst, nodA, nodB = plink
            if nodA.group != nodB.group :
                self.links.append((nodA,nodB))
                masterGroup = nodA.group
                slaveGroup  = nodB.group
                self.display("Will link %s->%s" % (nodA.label, nodB.label))
                self.links[-1] = (nodA,nodB)
                for node in self.nodes :
                    if node.group == slaveGroup :
                        node.group = masterGroup
                self.display("Grouped %s with %s" % (slaveGroup,masterGroup))
                nLinks += 1
        return nLinks

    def display (self, banner) :
        pgcon = self.pgcon
        pgcon.newScreen()
        for a,b in self.links :
            if a.group != b.group : color = WHITE
            else                  : color = colors[a.group%7]
            pgcon.lineDraw(color, a.pos, b.pos, 1)
        for node in self.nodes :
            color = colors[node.group%7]
            pgcon.textDraw(color, node.pos, node.label)
        pgcon.textDraw(WHITE, (self.pixels/2,10), banner)
        pgcon.camera.armed = 1
        pgcon.writeScreen(.500)

def euclDist2(a,b) :
    return (a[0]-b[0])**2 + (a[1]-b[1])**2

def randpos(low,high) :
    from random import randint
    return (randint(low,high), randint(low,high))

def main()  :
    from pgcon import Pgcon
    pgcon = Pgcon()
    seed    = sarg.Int("seed", 0)
    if seed : random.seed(seed)
    else :
        seed = random.randint(101,999)
        print "Seed is", seed
        random.seed(seed)
    pixels  = sarg.Int("pixels",600)
    nNodes  = sarg.Int("nodes",  20)
    ms = Minspan(pgcon, pixels, nNodes)
    nLinks = ms.linkNodes()
    print "Number of links", nLinks
    pgcon.close()

if __name__ == "__main__" : main()
