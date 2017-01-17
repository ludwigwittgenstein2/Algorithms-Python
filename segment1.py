#Segment 1
import csv

with open('/Users/Rick/Desktop/transaction_data.csv', 'rb') as f:
  next(f) # Remember Rick, this is to skip headers
  household_purchase = {}
  household_list = []
  data = csv.reader(f, delimiter=",")
  for row in data:
      if row[1] not in household_purchase:
          household_purchase[row[1]] = 1

      else:
          household_purchase[row[1]] += 1

for key, value in sorted(household_purchase.iteritems(), key=lambda(k,v): (v,k)):
    print "%s: %s" % (key,value)

for i, l in household_purchase.items():
    household_list.append([i, l])



print household_purchase
print household_list
