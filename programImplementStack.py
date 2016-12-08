"""Author:Rick Sam
        Date: Oct 19, 2016
        Comments: A Stack can be implemented using lists in Python, think of a stack of books
        it can be accessed in only one of its ends."""

class Stack(list):
        def __init__(self):
                self.items = []
        def isEmpty(self):
                return self.items == []
        def pop(self):
                if not self.isEmpty():
                        return self.items.pop()
                else:
                        return isEmpty
        def push(self,items):
                self.items.append(items)
        def size(self):
                return len(self.items)
        def peek(self):
                return self.items[-1]

def main():
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        print stack.peek()
        print stack.size()

if __name__ == '__main__':
        main()

