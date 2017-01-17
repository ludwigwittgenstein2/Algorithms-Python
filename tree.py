class Node():
    def __init__(self, val):
        self.value = val
        self.rightChild = None
        self.leftChild = None
        
    def insert(self, data):
        if self.value == data:
            return False
        
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True
        elif self.value < data:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True
            
    def find(self, data):
        
        if data == self.value:
            return True
        elif data > self.value:
            if self.rightChild:    
                return self.rightChild.find(data)
            else:
                return False
        elif data < self.value:
            if self.leftChild:    
                return self.leftChild.find(data)
            else:
                return False
            
    def preorder(self):
        if self:
            print str(self.value)
            
            if self.rightChild:
               self.rightChild.preorder()
            if self.leftChild:
                self.leftChild.preorder()
                
            
            
    def postorder(self):
        if self:
            if self.rightChild:
               self.rightChild.preorder()
            if self.leftChild:
                self.leftChild.preorder()
                
            print str(self.value)
        
        
    def inorder(self):
        if self:
            if self.rightChild:
               self.rightChild.preorder()
            
            print str(self.value)

            if self.leftChild:
                self.leftChild.preorder()
                
        
class Tree():
    def __init__(self):
        self.root = None
        
    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        
        else:
            self.root = Node(data)
            return True
        
    def preorder(self):
        print 'Preorder'
        self.root.preorder()
        
    def postorder(self):
        print 'Postorder'
        self.root.postorder()
    
    def inorder(self):
        print 'Inorder'
        self.root.inorder()
        
        
        
bst = Tree()
print bst.insert(5)
print bst.insert(10)
print bst.insert(7)

bst.preorder()
bst.postorder()
bst.inorder()

    
