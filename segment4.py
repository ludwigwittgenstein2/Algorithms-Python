#Segment 4, Say, I want to find out income group levels, in addition to household_key
import csv

with open('/Users/Rick/Desktop/sample_demographics.csv', 'r') as w:
    income_group = {}
    income_group_list = []
    next(w)
    data = csv.reader(w, delimiter=',')
    for row in data:
        if row[2] not in income_group:
            income_group[row[2]] = 1
        else:
            income_group[row[2]] += 1
    for key, value in sorted(income_group.iteritems(), key=lambda(k,v):(v,k)):
        print "%s: %s" % (key,value)

    for i, k in income_group.items():
        income_group_list.append([i,k])
        print income_group_list
