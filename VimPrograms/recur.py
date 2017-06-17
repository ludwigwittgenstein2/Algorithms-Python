#Find the closest related numbers


L = [10,5,3,1,8,4,9]
j = 0

if j <=len(L):
    for i in L:
        k = []
        k.append(L[j+1]-i)
        print L[j]
        print k
        j = j+1
