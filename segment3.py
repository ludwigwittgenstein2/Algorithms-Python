#Segment 3, Find out most purchased product, least purchased product


import csv

def segment3():
    with open('/Users/Rick/Desktop/sample_data.csv', 'r') as r:
        next(r) #This is to skip first header
        most_bought_product = {}
        most_bought_list = []
        data = csv.reader(r, delimiter=',')
        for row in data:
            if row[3] not in most_bought_product:
                most_bought_product[row[3]] = 1
            else:
                most_bought_product[row[3]] += 1
    for key, value in sorted(most_bought_product.iteritems(),key=lambda(k,v):(v,k)):
        print "%s: %s" % (key,value)
    for i, l in most_bought_product.items():
        most_bought_list.append([i,l])
        print most_bought_list

d = segment3()
print segment3
