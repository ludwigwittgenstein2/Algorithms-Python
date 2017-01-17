import yaml

def main():
    with open('/Users/Rick/Desktop/segments/data.yml', 'r') as r:
        CustomerSaleDict = yaml.load(r)
        r.close()
        count = 0
        bottom_list = []
        for household_key, value in sorted(CustomerSaleDict.items(), key=lambda k:(-k[1],k[0])):
            if count >10:
                break
            bottom_list.append(household_key)
            count +=1
        print bottom_list
if __name__=="__main__":
    main()
