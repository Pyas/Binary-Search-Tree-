class Node(object):
    def __init__(self,data):
        self.data=data
        self.nextNode=None
    def remove(self,data,previousNode):
        if self.data==data:
            previousNode.nextNode=self.nextNode
            #del self.data
            del self
        else:
            if self.nextNode:
                self.nextNode.remove(data,self)
