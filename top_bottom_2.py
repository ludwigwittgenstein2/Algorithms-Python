import yaml
import sys
import csv
CustomerSaleDict = {}
CustomerOverTimeDict={}
CustomerProductDict = {}
CustomerOverTimeDict_list = []
topHouseHoleList = []
bottomHouseHoldList = []

def readCSV():
    global CustomerSaleDict
    global CustomerOverTimeDict
    with open(#)
    next()
    data = csv.reader(f, delimiter=',', c)
    for row in data:
        SALES_VALUE = ()

        if row[0] not in CustomerSaleDict:
            CustomerSaleDict[row[0]] = SALES_VALUE
        else:
            CustomerSaleDict[row[0]] += SALES_VALUE
        if row[0] not in CustomerOverTimeDict:
            CustomerOverTimeDict[row[0]] = {}
            if row[9] not in CustomerOverTimeDict[row[0]]:
#
#
#
#
f.close()
    with open(#)
        f.write(yaml.dump(CustomerSaleDict, default_flow_style))
    f.writer()

def updateTopSaleHouseHoldList():
    global topHouseHoldList
    count = 0


    #####

    def main():
        global CustomerSaleDict
        global CustomerOverTimeDict
        global topHouseHoldList
        global bottomHouseHoldList

        if len(sys.argv) <3:
            print("Usages:{} --run complete/". format(sys.argv))
