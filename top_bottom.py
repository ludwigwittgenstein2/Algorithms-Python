import yaml

def main():
  with open('/Users/Rick/Desktop/segments/data.yml', 'r') as w:
      with open('/Users/Rick/Desktop/segments/CustomerOverTimeDict.yml', 'r') as f:
          CustomerOverTimeDict = yaml.load(f)
          CustomerSaleDict = yaml.load(w)
          f.close()
          w.close()
          count = 0
          toplist = []
          for household_key, value in sorted(CustomerSaleDict.items(), key=lambda k:k[1]):
              if count>10:
                  break
              toplist.append(household_key)
              count +=1
              print toplist
#Bottom List of Customers
          bottom_list=[]
          count = 0
          for household_key, value in sorted(CustomerSaleDict.items(), key=lambda k:k[1], reverse= True):
              if count >10:
                  break
              bottom_list.append(household_key)
              count +=1
              print bottom_list
          for household_key, value in CustomerOverTimeDict.items():
              if household_key in toplist:
                Weekly_list = [['week_no', 'sales_value']]
                for week_no, sales_value in value.items():
                    Weekly_list.append([week_no,sales_value])
                    print household_key, Weekly_list


if __name__=="__main__":
    main()
