def ins_sort_rec(seq, i):
    if i == 0:
        return
    ins_sort_rec(seq, i-1)
    print "recursion:", i-1
    j = i
    print j
    while j > 0 and seq[j-1] > seq[j]:
        print "Before Sort", seq[j-1], seq[j]
        seq[j-1], seq[j] = seq[j], seq[j-1]
        print "After Sort", seq[j-1], seq[j]
        j -= 1


def main():
    seq = [11,9,5,4,2]
    ins_sort_rec(seq,4)
    print seq

if __name__ == '__main__':
    main()
