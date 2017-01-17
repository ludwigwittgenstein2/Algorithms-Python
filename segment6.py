#Create a dictionary  [key -->(household key,product id) with
#counter -->value]
#Household key and product id must be in a tuple
import csv

with open('/Users/Rick/Desktop/sample_data.csv', 'r') as w:
    next(w)
    purchase_made_household = {}
    product = ()
    count = 1
    data = csv.reader(w, delimiter=',')

    for row in data:
        product = (row[0],row[3])
    if row[1] not in purchase_made_household:
        purchase_made_household[product] = 1
    else:
        purchase_made_household[product] += 1

print purchase_made_household
