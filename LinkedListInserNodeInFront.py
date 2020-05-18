class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertFornt(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        

    def printLinkedList(self):
        tmp = self.head
        while tmp is not None:
            print(tmp.data)
            tmp = tmp.next


linked_list = LinkedList()

linked_list.insertFornt("Hanik")
linked_list.insertFornt("1")
linked_list.insertFornt("2")

linked_list.printLinkedList()