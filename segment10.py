import yaml

def main():
  with open('/Users/Rick/Desktop/segments/data.yml', 'r') as w:
    CustomerSaleDict = yaml.load(w)
    w.close()
    count = 0
    toplist = []
    for household_key, value in sorted(CustomerSaleDict.items(), key=lambda k:k[1]):
        if count>10:
            break
        toplist.append(household_key)
        count +=1
    print(toplist)
if __name__=="__main__":
    main()
