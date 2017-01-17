seq = [20, 10, 24, 56, 89, 99]

def trav(seq, i=0):
    if i ==len(seq):
        return
    trav(seq, i+1)

if __name__ == '__main__':
    trav(range(100))
