class Node:
    def __init__(self, data):
        self.data = data
        self.nextAddress = None
        

class LinkedList:
    def __init__(self):
        self.hade = None
    
    def printList(self):
        tmp = self.hade
        while(tmp != None):
            print(tmp.data)
            tmp = tmp.nextAddress
    
    def insertNode(self, value):
        newNode = Node(value)
        if self.hade == None:
            self.hade = newNode
        else:
            lastElemet = self.hade
            while (lastElemet.nextAddress != None):
                lastElemet = lastElemet.nextAddress
            lastElemet.nextAddress = newNode


linked_list = LinkedList()



linked_list.insertNode("anik")
linked_list.insertNode("shakil")
linked_list.insertNode("Niloy")
linked_list.printList()

