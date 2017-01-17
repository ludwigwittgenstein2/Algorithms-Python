def bubble_Sort(item):
    """Bubble Sort is cool"""
    print "The item before sorting:", item
    for i in range(len(item)):
        print "The first loop of i:", i
        for j in range(len(item)-1-i):
            print "The second loop of j:", j
            if item[j] > item[j+1]:
                 print "The item before switching", item[j],item[j+1]
                 item[j],item[j+1] = item[j+1], item[j]
                 print "The item after switching", item[j], item[j+1]

    print "The final number after Bubble Sort:", item

bubble_Sort([50,49,1,24,32,99,5,67,23,31])

