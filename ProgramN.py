def total(initial=5, *numbers, **keywords):
    print initial
    count = initial # 5
    print count
    for number in numbers:
        print number # Number in [10,1,2,3]
        count += number # How is this 11?
        print 'This is number loop:',count # 5 = 5 + 10= 15, 65+1 = 66, 156 + 2
    for key in keywords: # key is 50 in vegetables
        count += keywords[key]
        print 'This is keywords loop:',count # 5 = 15 + 50 = 65,
    return count

print total(10,1,2,3,vegetables=50, fruits=100)
