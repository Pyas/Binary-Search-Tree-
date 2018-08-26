from BinarySearchTreeDS.Node import Node;
class BST(object):
    def __init__(self):
        self.root=None
    def insert(self,data):
        if not self.root:
            self.root=Node(data)
        else:
            self.root.insert(data)
    def remove(self,dataToRemove):
        if self.root is not None:
            if self.root.data==dataToRemove:
                tempNode=Node(None)
                tempNode.leftChild=self.root
                self.root.remove(dataToRemove,tempNode)
            else:
               self.root.remove(dataToRemove,None)
    def getMax(self):
        if self.root:
            return self.root.getMax()
    def getMin(self):
        if self.root:
            return self.root.getMin()
    def traverseInOrder(self):
        if self.root:
            self.root.traverseInOrder()
    def getNode(self,data):
        if self.root:
            self.root.getNode(data)
        else:
            print("The tree is not set yet")