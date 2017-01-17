from pandas import DataFrame
from math import log
import json

df = DataFrame.from_csv("data2cluster.txt", sep="\t")
dfval = df.values


from scipy.stats.mstats import zscore

df_zscore= zscore(dfval)

from scipy.cluster.vq import kmeans,vq

centroids,_ = kmeans(dfval,4)
# assign each sample to a cluster
idx,_ = vq(dfval,centroids)

file_kmeans = open('kmeans_netid.txt','w+')

for i in range(1,len(idx)):
    file_kmeans.write( str(df.iloc[i].name)+'\t'+str(idx[i]) + '\n' )
    
file_kmeans.close()

