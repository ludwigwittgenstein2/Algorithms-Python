#Find household household_key_high_income and what are they buying?
#household_key_high_income group is classified as people who buy more than 5
#House hold heavy users, In order to find this, I need to store household_key as key
#And sales value as value and then add the sales value

import csv

with open('/Users/Rick/Desktop/sample_data.csv', 'r') as w:
    next(w)
    data = csv.reader(w, delimiter=',')
    find_high_products = {}
    high_income_house_holds = []
    new_data = ()
    household_key_high_income = {}

    for row in data:
        SALES_VALUE = (row[5])
        if row [0] not in household_key_high_income:
            household_key_high_income[SALES_VALUE] = 1

        else:
            household_key_high_income[SALES_VALUE] += 1

    for k, j in household_key_high_income.items():
        if j > 5:
            high_income_house_holds.append([k])
#Now that I have high_income_House hold, I need to find their purchase products
    for row in data:
        new_data = (high_income_house_holds,row[3])
    if row[0] not in new_data:
        find_high_products[new_data] = 1
    else:
        find_high_products[new_data] += 1

print household_key_high_income
