class Node(object):
    def __init__(self,data):
        self.leftChild=None
        self.rightChild=None
        self.data=data
    def insert(self,data):
        if data<=self.data:
            if not self.leftChild:
                self.leftChild=Node(data)
            else:
                self.leftChild.insert(data)
        else:
            if not self.rightChild:
                self.rightChild=Node(data)
            else:
                self.rightChild.insert(data)
    def getMin(self):
        if not self.leftChild:
            return self.data
        else:
            return self.leftChild.getMin()
    def getMax(self):
        if self.rightChild==None:
            return self.data
        else:
            return self.rightChild.getMax()
    def traverseInOrder(self):
        if self.leftChild:
            self.leftChild.traverseInOrder()
        print(self.data)
        if self.rightChild:
            self.rightChild.traverseInOrder()

    def remove(self,data,parentNode):
        if data<self.data:
            if self.leftChild:
                self.leftChild.remove(data,self)
        elif data>self.data:
            if self.rightChild:
                self.rightChild.remove(data,self)
        else:
            if self.rightChild and self.leftChild:
                self.data=self.rightChild.getMin()
                self.rightChild.remove(self.data,self)
            elif parentNode.leftChild==self:
                if self.leftChild:
                    tempNode=self.leftChild
                else:
                    tempNode=self.rightChild
                parentNode.leftChild=tempNode
            elif parentNode.rightChild==self:
                if self.leftChild:
                    tempNode=self.leftChild
                else:
                    tempNode=self.rightChild
                parentNode.rightChild=tempNode
    def getNode(self,data):
        if data<self.data:
            if self.leftChild:
                self.leftChild.getNode(data)
            else:
                print('No match !')
        elif data>self.data:
            if self.rightChild:
                self.rightChild.getNode(data)
            else:
                print("No match")
        else:
            print(self)



