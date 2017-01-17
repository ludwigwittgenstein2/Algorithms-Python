"""
  Author: Rick Sam
  Book: Algorithms for Python
  Comment: Learning

"""

def ins_sort(seq, i):
    if i ==0:
        return
    ins_sort(seq, i-1)
    j = 1
    while j >0 and seq[j-1] > seq[j]:
        seq[j-1], seq[j] = seq[j], seq[j-1]
        j -= 1

if __name__ == '__main__':
    seq = [10,2,6,3,1,5]
    print ins_sort(seq, 5)
