"""
Gnome_Sort
<<<<<<< HEAD
        -- i = 0
        i < 5:
            if

CARDS: [J], [10], [A], [5], [7], [K]
=======
>>>>>>> d4c3f76d4577dc9d028d11c36f869687a727e23f

"""

import timeit

def Gnome_sort(seq):
    i = 0
    while i < len(seq):
        if i == 0 or seq[i-1] < seq[i]:
            i = i + 1
        else:
            seq[i-1], seq[i] = seq[i], seq[i-1]
            i = i - 1


def main():
    from timeit import Timer
    seq = [10,9,8,7,6,5,4,3,2,1,10,9,8,7,6,5,4,3,2,1,10,9,8,7,6,5,4,3,2,1,10,9,8,7,6,5,4,3,2,1,10,9,8,7,6,5,4]
    Gnome_sort(seq)
    t = Timer(lambda:Gnome_sort(seq))
    print t.timeit(number=1)

if __name__ == '__main__':
    main()
