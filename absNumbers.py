"""So Rick, you have a list of numbers and you need to find the closest two numbers,
so think of [100, 20, 90, 21,22], in this, you need to find the closest two numbers,
how will you do it?
I can solve this by going through the list, and then
what do I do next? I say, find diff between [i] and [i+1]
Store in in variable
And then I need another loop to run through the list
And find the smallest
and I need to find the diff between i+1 and i.
And, the least amount is the final answer.
store it in a variable
"""
import cProfile

def smallest_induction(small):
        for i in small:
                for j in small:
                        if i==j:
                                continue
                        if i-j <0:
                                continue
                        print i-j



def find_closest(seq):
        nList = []
        for i in seq:
                for j in seq:
                        if i==j:
                                continue
                        if i-j <0:
                                continue
                        diff = i-j
                        nList.append(diff)
        for k in nList:
                tmp = nList[0]
                if k < tmp:
                        tmp = k
        print tmp

def sorted_list(seq):
        seq.sort()
        nList = []
        for i in range(len(seq)-1):
                x, y = seq[i], seq[i+1]
                if x == y:
                        continue
                if y - x <0:
                        continue
                diff =abs(x-y)
                nList.append(diff)
#               nList.append(diff)
#        print nList
        for i in nList:
                tmp = nList[0]
                if i < tmp:
                        tmp = i
        print tmp

def main():
        seq = [100,20,90,21,22]
        find_closest(seq)
        small = [100,20]
        smallest_induction(small)
        sorted_list(seq)
if __name__ == '__main__':
        main()
        cProfile.run('main()')


