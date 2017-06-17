"""
# Author: Rick
# Date: June 16, 2017
# Purpose: Gnome Sort in real world
# Name: Gnome Sort

[Pot7], [Pot1], [Pot2], [Pot5], [Pot4], [Pot 6], [Pot3]
Comparions - (n-1), so comparions = 6
Gnome Sort

"""

def Gnome_sort(seq):
    i = 0
    while i < len(seq):
        if i == 0 or seq[i-1] < seq[i]:
            i = i + 1
        else:
            seq[i], seq[i-1] = seq[i-1], seq[i]
            i = i - 1


def main():
    seq = [10,9,6,5,3,1]
    Gnome_sort(seq)
    print seq



if __name__ == '__main__':
    main()
