from LinkedList.Node import Node;
class LinkList(object):
    def __init__(self):
        self.head=None
    def insertFirst(self,data):
        newNode=Node(data)
        if not self.head:
            self.head=newNode
        else:
            newNode.nextNode=self.head
            self.head=newNode
    def insertLast(self,data):
        newNode=Node(data)
        if not self.head:
            self.insertFirst(data)
        else:
            actualNode=self.head.nextNode
            while actualNode is not None:
                 if actualNode.nextNode==None:
                     actualNode.nextNode=newNode
                     actualNode.nextNode.nextNode=None
                 actualNode=actualNode.nextNode
    def remove(self,data):
        if self.head:
            if data==self.head.data:
                self.head=self.head.nextNode
            else:
                #self.head.remove(data,self.head)
                currentNode=self.head
                while currentNode.nextNode is not None:
                    # if currentNode.nextNode and currentNode.nextNode.data==data:
                    #     temp=currentNode.nextNode
                    #     currentNode.nextNode=currentNode.nextNode.nextNode
                    #     print('this is temp',temp.data)
                    #     del temp
                    #     break
                    # currentNode=currentNode.nextNode
                    if currentNode.nextNode.data==data:
                        temp=currentNode.nextNode
                        currentNode.nextNode=currentNode.nextNode.nextNode
                        del temp
                        break
                    currentNode=currentNode.nextNode

    def traverseList(self):
        currentNode=self.head
        while currentNode is not None:
            print("%d"%currentNode.data)
            currentNode=currentNode.nextNode
