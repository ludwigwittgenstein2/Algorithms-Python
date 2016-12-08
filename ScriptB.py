import yaml
import csv

productNumberTimes = {}
purchaseTimes = 1


with open('/Users/Rick/Desktop/projectFinalFolder/segments/consumerPurchaseAllProductDetails.yaml', 'r') as w:
    ProductDetails = yaml.load(w)
w.close()

for row in ProductDetails.keys():
    for quarter in ProductDetails[row].keys(): # Quarter is actually Product_ID number
        for sub in ProductDetails[row][quarter].keys():
            for product_id in ProductDetails[row][quarter][sub].keys():
                if product_id == product_id: # Product_ID here is SUB_COMMODITY NAME, EG: POTATO CHIPS
                    if row not in productNumberTimes:
                        productNumberTimes[row]= {}
                        productNumberTimes[row][quarter] = {}
                        productNumberTimes[row][quarter][product_id] = {}
                        productNumberTimes[row][quarter][product_id] = purchaseTimes
                    else:
                        if quarter not in productNumberTimes[row]:
                            productNumberTimes[row][quarter] = {}
                            productNumberTimes[row][quarter][product_id] = {}
                            productNumberTimes[row][quarter][product_id] = purchaseTimes
                        else:
                            if product_id not in productNumberTimes[row][quarter]:
                                productNumberTimes[row][quarter][product_id] = {}
                                productNumberTimes[row][quarter][product_id] = purchaseTimes
                            else:
                                productNumberTimes[row][quarter][product_id] += purchaseTimes


with open('/Users/Rick/Desktop/script_B_Results.yaml', 'w') as w:
    w.write(yaml.dump(productNumberTimes, default_flow_style=False))
w.close()





