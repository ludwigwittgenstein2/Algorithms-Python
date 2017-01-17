
'''
_______________________________________
 Created on Sep 16, 2015
 @author:
_________________________________________
 ''''

import yaml
import sys
import csv

CustomerSaleDict={}
CustomerOverTimeDict={}
productDict = {}
topHouseHoldList = []
bottomHouseHoldList = []

def readCSV():
    global customerSaleDict
    global customerOverTimeDict

    with open(#) as f:
        data = csv.reader(f, delimiter=',')
        next(data)
    for row in data:
        salesValue = (round(float(row[5])))

        if row[0] not in customerSaleDict:
            customerSaleDict[row[0]]=salesValue
        else:
            customerSaleDict[row[0]] += salesValue
        if row[9] not in customerOverTimeDict[row[0]]:
            customerOverTimeDict[row[0]][row[9]] = salesValue
        else:
            customerOverTimeDict[row[0][row[9]]] += salesValue
    f.close()

    with open(#):
        f.write()
    f.close()

    with open(""):
        f.write
    f.close()

    def buildTopSaleHouseHoldList():
        global topHouseHoldList
        count = 0
        for houseHoldKey, salesValue in sorted(customerSaleDict.items(), key=lambda k:k[1],reverse=True):
            if count >10:
                break
            topHouseHoldList.append(houseHoldKey)
            count +=1

        print topHouseHoldList
        with open():
            f.write(yaml.dump())
        f.close()

    def generatePlotTopSaleData():

        for houseHoldKey, weekdict in customerOverTimeDict.items():
            if houseHoldKey in topHouseHoldList:
                Weekly_list=[[]]
                for weekNo, salesValue in sorted(b)
