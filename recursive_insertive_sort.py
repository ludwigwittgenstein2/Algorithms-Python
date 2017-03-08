#!/usr/bin/Python

def ins_sort_rec(seq, i):
    if i == 0:
        return ins_sort_rec(seq, i-1)
        j = i
    while j >0 and seq[j-1] > seq[j]:
        seq[j-1], seq[j] = seq[j], seq[j-1]
        j -= 1
    print ins_sort_rec(seq,1)

def main():
    ins_sort_rec(seq, i)

if __name__ == '__main__':
    seq = [10,4,2,4,1]
    main()
