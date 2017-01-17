#trees
class Tree:
    def __init__(self, left,right):
        self.left = left
        self.right = right

class MultiTree:
    def __init__(self,kids,next=None):
        self.kids =self.val=kids
        self.next = next

def tree():
    T = [["a","b"],["c"],["d",["e","f"]]]
    print T[0][1]

def main():
    t = MultiTree(MultiTree("a",MultiTree("b",MultiTree("c",MultiTree("d")))))
    print t.kids.next.next.val


if __name__ == '__main__':
    main()
