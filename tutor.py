#tutor.py


def main():
    with open('/Users/Rick/Desktop/segments/data.yml', 'r') as f:
        CustomerSaleDict = yaml.load(f)
        f.close()
        count = 0
        bottomlist = []
        for household_key,value in sorted(CustomerSaleDict.items(), key=lambda k:k[1]):
            if count >10:
                break
            bottomlist.append([household_key,value])
            count += 1
            print(bottomlist)
        count = 0
        toplist = []
        for household_key,value in sorted(CustomerSaleDict.items(), key=lambda k:k[1],reverse=True):
            if count >10:
                break
        toplist.append([household_key,value])
            count += 1
        print(toplist)
if __name__ == "__main__":
    main()
