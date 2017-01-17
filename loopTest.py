def bubble(item):
    for i in range(len(item)):
        print "This is first loop:i", i
        for j in range(len(item)-1-i):
            print "this is J loop:", j
            if item[j]> item[j+1]:
                print "this is before switch", item[j], item[j+1]
                item[j], item[j+1] = item[j+1], item[j]
                print "This is after you switch:", item[j], item[j+1]
    print item

item = [10,9,8,7,6,5,4,3,2,1]
bubble(item)


