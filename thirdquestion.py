"""
a.) from first question result for bottom 5 or 10 customer, store their household_key in a list.
b). read full csv and 2d build Dictionary for those household_key, customerProductDict which has their product_ID as another level key for dictionary and household_key as key for dictionary.
household_key, customerProductDict which has their product_ID as another level key for dictionary and household_key as key for dictionary.
customerProductDict = { '208' : {'101212313': (,,)} , '407': {'23232132':(,,)}}

"""
import yaml
import sys
import csv

topHouseHoldList = []
customerProductDict = {}

def readCSV():
    global topHouseHoldList
    global customerProductDict
    with open("/Users/Rick/Desktop/segments/topHouseHoldList", 'r') as w:
        data = yaml.load(w)

    with open("/Users/Rick/Desktop/CSV/transaction_data2.csv", 'r') as f:
        data = csv.reader(f, delimiter=',')
        next(data)
    for row in data:
        if row[0] not in topHouseHoldList:
            customerProductDict[row[0]] = {}

            if row [3] not in customerProductDict[row[0]]:
                customerProductDict[row[0][row[3]] = {}
                customerProductDict[row[0][row[3][row[4][row[5][row[6]]]]]] = []
            else:
                if row [3] not in customerProductDict[row[0]][row[3]]:
                    customerProductDict[row[0]][row[3]][row[4]] = []
        else:
            if row[3] not in customerProductDict[row[0]]:
