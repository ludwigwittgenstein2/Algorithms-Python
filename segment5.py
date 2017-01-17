#House hold heavy users, In order to find this, I need to store household_key as key
#And sales value as value and then add the sales value

import csv
import yaml

def main():
    with open('/Users/Rick/Desktop/CSV/transaction_data2.csv', 'r') as w:
        next(w)
        CustomerSaleDict={} #This is the total expenses
        global CustomerOverTimeDict
        CustomerOverTimeDict = {}
        CustomerProductDict = {}
        CustomerOverTimeDict_list = [] #This is empty list
        data = csv.reader(w, delimiter=',')
        w.close()
        for row in data:
            SALES_VALUE = (round(float(row[5])))
            if row[0] not in CustomerSaleDict:
                CustomerSaleDict[row[0]] = SALES_VALUE
            else:
                CustomerSaleDict[row[0]]+= SALES_VALUE
            if row[0] not in CustomerOverTimeDict:
                CustomerOverTimeDict[row[0]]= {}
                if row[9] not in CustomerOverTimeDict[row[0]]:
                    CustomerOverTimeDict[row[0]][row[9]] = SALES_VALUE
                else:
                    CustomerOverTimeDict[row[0]][row[9]] += SALES_VALUE
            else:
                if row[9] not in CustomerOverTimeDict[row[0]]:
                    CustomerOverTimeDict[row[0]][row[9]]= SALES_VALUE
                else:
                    CustomerOverTimeDict[row[0]][row[9]] += SALES_VALUE
if __name__=="__main__":
    main()
