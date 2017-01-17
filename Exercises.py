def recursive_sum(nested_num_list):
    sum = 0
    for element in nested_num_list:
        if type(element) == type([]):
            sum = sum + recursive_sum(element)
        else:
            sum = sum +element
    return sum

if __name__ == '__main__':
    recursive_sum([1,2,5,6])
