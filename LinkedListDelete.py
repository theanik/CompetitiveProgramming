class Node:
    def __init__(self, data):
        self.data = data
        self.nextAddress = None
        

class LinkedList:
    def __init__(self):
        self.head = None
    
    def printList(self):
        tmp = self.head
        while(tmp != None):
            print(tmp.data)
            tmp = tmp.nextAddress
    
    def insertNode(self, value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
        else:
            lastElemet = self.head
            while (lastElemet.nextAddress != None):
                lastElemet = lastElemet.nextAddress
            lastElemet.nextAddress = newNode
    def deleteNode(self, position):
        if position == 0:
            tmp = self.head
            self.head = tmp.nextAddress
            tmp = None
        else:
            tmp = self.head
            for _ in range(position - 1):
                tmp = tmp.nextAddress
            tmp2 = self.head
            tmp2 = tmp.nextAddress
            tmp.nextAddress = tmp2.nextAddress
linked_list = LinkedList()



linked_list.insertNode("anik")
linked_list.insertNode("shakil")
linked_list.insertNode("Niloy")
linked_list.insertNode("1")
linked_list.insertNode("3")

linked_list.deleteNode(0)
linked_list.printList()


# def deleteNode(head, position):
#     if position == 0: 
#         return head.next
#     head.next = deleteNode(head.next, position-1)
#     return head