import math

import sys

dE = {'A':0.25,'C':0.25,'G':0.25,'T':0.25}

d5 = {
    'A':0.05,
    'C':0.0,
    'G':0.95,
    'T':0.0
    }

d5second = {
    'A':0.05,
    'C':0.05,
    'G':0.10,
    'T':0.80
}

dI = {
    'A':0.4,
    'C':0.1,
    'G':0.1,
    'T':0.4
    }

dTrans = {'EE':0.9,'E5':0.1,'5I':1.0,'II':0.9,'StartE':1.0,'IEnd':0.1}

seq = sys.argv[1]

paths = {}
path_count = 0

paths[0] = [['E'],dTrans['StartE']*dE[seq[0]]]

for i, nuc1 in enumerate(seq[1:]):

    if dTrans['E5']*d5[nuc1] >= 0.001:    
        path_count = path_count + 1
        paths[path_count] = [list(paths[0][0]),float(paths[0][1])]
        paths[path_count][0].append('5')
        paths[path_count][1] = paths[path_count][1]*dTrans['E5']*d5[nuc1]*d5second[nuc1]
        
        if seq[1:][i+1:]:
        
            paths[path_count][0].append('I')
            paths[path_count][1] = paths[path_count][1]*dTrans['5I']*dI[seq[1:][i+1]]
            
            if seq[1:][i+2:]:
            
                for nuc2 in seq[1:][i+2:]:
                
                    paths[path_count][0].append('I')
                    paths[path_count][1] = paths[path_count][1]*dTrans['II']*dI[nuc2]*dTrans['IEnd']

    paths[0][0].append('E')
    
    paths[0][1] = paths[0][1]*dTrans['EE']*dE[nuc1]
    
    
    
del paths[0]
path_sum=0.0

for p in paths:

    path_sum = path_sum + paths[p][1]

for p in paths:

    print paths[p][0],math.log(paths[p][1]),paths[p][1]/path_sum