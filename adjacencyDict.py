#Adjacencydicts with Edge Weights

def adjacencyList():
    a,b,c,d,e,f,g,h = range(8)
    N = [{b:2,c:1,d:3,e:9,f:4},
        {c:4,e:3},
        {d:8},
        {e:7},
        {f:5},
        {c:2, g:2,h:2},
        {f:1,h:6},
        {f:9,g:8}
]
    print N[f]
    print N[c]

def adjacencyMatrix():
    a, b, c, d, e, f, g, h = range(8)
    _ = float('inf')

    #     a b c d e f g h
    W = [[0,2,1,3,9,4,_,_], # a
        [_,0,4,_,3,_,_,_], # b
        [_,_,0,8,_,_,_,_], # c
        [_,_,_,0,7,_,_,_], # d
        [_,_,_,_,0,5,_,_], # e
        [_,_,2,_,_,0,2,2], # f
        [_,_,_,_,_,1,0,6], # g
        [_,_,_,_,_,9,8,0]] # h

    print "Hello"

def main():
    adjacencyMatrix()

if __name__ == 'main':
    main()
