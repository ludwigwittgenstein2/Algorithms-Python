#2d list datatype

elements = []
elements.append([])
elements.append([])

elements[0].append(1)
elements[0].append(2)

elements[1].append(3)
elements[1].append(4)



for row in elements:
    for column in row:
        print column
    print row 
