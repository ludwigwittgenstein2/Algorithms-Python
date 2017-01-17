import sys

from pandas import DataFrame
from math import log

def parta(data_file,output):
    df = DataFrame.from_csv(data_file, sep="\t")

    from scipy import stats
    
    f = open(output,'w+')
    
    for row in df.iterrows():
        
        rootCtrlMean =  ( row[1]['RootCtrl1'] + row[1]['RootCtrl2'] + row[1]['RootCtrl3'] ) / 3
        rootTrmtMean =  ( row[1]['RootTrt1'] + row[1]['RootTrt2'] + row[1]['RootTrt3'] ) / 3
        
        if abs(log(rootCtrlMean,2)-log(rootTrmtMean,2)) >= 3 :
            
            rootTrmtArr = [ log(row[1]['RootCtrl1'],2) , log(row[1]['RootCtrl2'],2) , log(row[1]['RootCtrl3'],2) ]
            rootCtrlArr = [ log(row[1]['RootTrt1'],2) , log(row[1]['RootTrt2'],2) , log(row[1]['RootTrt3'],2) ]
            
            if stats.ttest_ind(rootTrmtArr,rootCtrlArr).pvalue < 0.05:
                f.write( row[0] + '\n')
                
    f.close()

def kmeans(data_file,output):
    df = DataFrame.from_csv(data_file, sep="\t")
    dfval = df.values
    
    
    from scipy.stats.mstats import zscore
    
    df_zscore= zscore(dfval)
    
    from scipy.cluster.vq import kmeans,vq
    
    centroids,_ = kmeans(dfval,4)
    # assign each sample to a cluster
    idx,_ = vq(dfval,centroids)
    
    file_kmeans = open(output,'w+')
    
    for i in range(1,len(idx)):
        file_kmeans.write( str(df.iloc[i].name)+'\t'+str(idx[i]) + '\n' )
        
    file_kmeans.close()


def partb(data_file,output):
    df = DataFrame.from_csv(data_file, sep="\t")


    import scipy.cluster.hierarchy as hc
    
    dfVals = df.values
    
    Z = hc.linkage(df, metric='correlation', method='average')
    # 
    # print Z[0]
    # dZ = hc.dendrogram(Z)
    #
    
    f = open(output,'w+')
    
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

if __name__ == '__main__':
    arguments = sys.argv[1:]
    
    file_input = arguments.index('-f')
    file_input = arguments[file_input+1]
    
    file_interested = arguments.index('-g')
    file_interested = arguments[file_interested+1]
        
    file_heirarichal = arguments.index('-h')
    file_heirarichal = arguments[file_heirarichal+1]
    
    file_kmean = arguments.index('-k')
    file_kmean = arguments[file_kmean+1]
    
    parta(data_file=file_input,output=file_interested)
    
    partb(data_file=file_input,output=file_heirarichal)
    
    kmeans(data_file=file_input,output=file_kmean)