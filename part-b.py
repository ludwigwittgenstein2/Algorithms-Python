from pandas import DataFrame
from math import log
import json

df = DataFrame.from_csv("data2cluster.txt", sep="\t")


import scipy.cluster.hierarchy as hc

dfVals = df.values

Z = hc.linkage(df, metric='correlation', method='average')
# 
# print Z[0]
# dZ = hc.dendrogram(Z)
#

f = open('file_name.txt','w+')

clstNum = hc.fcluster(Z, 1)
for i in clstNum:
    f.write( str(i)+'\n')
    
f.close()
print len(list(set(clstNum)))
# 
# f = open('file_name.txt','w+')
# f.write(json.dumps(Z))
# f.close()

# x = hc.fcluster(df, 4, criterion='distance')
# print x