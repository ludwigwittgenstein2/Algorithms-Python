#Adjacencydicts with Edge Weights

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

print N

print N[a][d]
