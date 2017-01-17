#Find out product_id, which has sold a lot

import csv

with open('/Users/Rick/Desktop/sample_data.csv', 'r') as w:
    next(w)
    product_sales = {}
    data = csv.reader(w, delimiter=',')
    for row in data:
        if row[3] not in product_sales:
            product_sales[row[3]] = 1
        else:
            product_sales[row[3]] += 1

print product_sales
