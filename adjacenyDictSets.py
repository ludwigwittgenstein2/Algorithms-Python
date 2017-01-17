#AdjacencyDict with sets

a,b,c,d,e,f,g,h = range(8)

N = {'a':set('bcdef'),
    'b':set('ce'),
    'c':set('d'),
    'd':set('e'),
    'e':set('f'),
    'f':set('cgh'),
    'g':set('fh'),
    'h':set('fg')}
print N['a']
