import random

one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
seven = 0
eight = 0
nine = 0
ten = 0
count = 0

while count < 10:
    random_list = random.randint(1, 10)
    print random_list

    if random_list == 1:
        one += 1
    elif random_list == 2:
        two += 1
    elif random_list == 3:
        three += 1
    elif random_list == 4:
        four += 1
    elif random_list == 5:
        five += 1
    elif random_list == 6:
        six += 1
    elif random_list == 7:
        seven += 1
    elif random_list == 8:
        eight += 1
    elif random_list == 9:
        nine += 1
    else:
        ten += 1
    count += 1

print("1 occured " + str(one) + " times")
print("2 occured " + str(two) + " times")
print("3 occured " + str(three) + " times")
print("4 occured " + str(four) + " times")
print("5 occured " + str(five) + " times")
print("6 occured " + str(six) + " times")
print("7 occured " + str(seven) + " times")
print("8 occured " + str(eight) + " times")
print("9 occured " + str(nine) + " times")
print("10 occured " + str(ten) + " times")
