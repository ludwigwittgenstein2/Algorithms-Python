def sel_sort_rec(seq, i):
    if i == 0:
        return
    max_j = i
    for j in range(i):
        if seq[j] > seq[max_j]:
            max_j = j
    seq[i], seq[max_j] = seq[max_j], seq[i]
    sel_sort_rec(seq, i-1)


def main():
    sel_sort_rec([9,5,4,2,1], 1)



if __name__ == '__main__':
    main()
