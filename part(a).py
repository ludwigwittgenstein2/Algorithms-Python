from pandas import DataFrame
from math import log

df = DataFrame.from_csv("data2cluster.txt", sep="\t")

from scipy import stats

f = open('file_name.txt','w+')

for row in df.iterrows():
    
    rootCtrlMean =  ( row[1]['RootCtrl1'] + row[1]['RootCtrl2'] + row[1]['RootCtrl3'] ) / 3
    rootTrmtMean =  ( row[1]['RootTrt1'] + row[1]['RootTrt2'] + row[1]['RootTrt3'] ) / 3
    
    if abs(log(rootCtrlMean,2)-log(rootTrmtMean,2)) >= 3 :
        
        rootTrmtArr = [ log(row[1]['RootCtrl1'],2) , log(row[1]['RootCtrl2'],2) , log(row[1]['RootCtrl3'],2) ]
        rootCtrlArr = [ log(row[1]['RootTrt1'],2) , log(row[1]['RootTrt2'],2) , log(row[1]['RootTrt3'],2) ]
        
        if stats.ttest_ind(rootTrmtArr,rootCtrlArr).pvalue < 0.05:
            f.write( row[0] + '\n')
            
f.close()