#Segment 2, Find out Revenue of store
# So, first, I go to the column 5, and then store it as a List


def total_revenue():
    empty_list = []
    with open('\Users\Rick\Desktop\sample_data.csv', 'r') as w:
        next(w)
        data = csv.reader(w, delimiter=',')
        for row in data:
            if row[5] not in empty_list:
                pass
            else:
                empty_list.append()

print empty_list
