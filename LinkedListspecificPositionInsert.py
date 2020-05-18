class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    

class LinkedList:
    def __init__(self):
        self.head = None

    def insertFornt(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def insertInNth(self, data,position):
        ptr = self.head
        curerntPosition = 1
        newNode = Node(data)
        if position == 0:
            newNode.next = self.head
            self.head = newNode
        else:
            while ptr.next is not None:
                if curerntPosition == position:
                    newNode.next = ptr.next
                    ptr.next = newNode
                    break
                curerntPosition += 1
                ptr = ptr.next


    
    def printLinkedList(self):
        tmp = self.head
        while tmp is not None:
            print(tmp.data)
            tmp = tmp.next

linked_list = LinkedList()

linked_list.insertFornt("anik")
linked_list.insertFornt("shakil")
linked_list.insertFornt("Niloy")
linked_list.insertInNth("new",2)
linked_list.insertInNth("new",2)
linked_list.insertInNth("Zero",0)
linked_list.insertInNth("Five",5)


linked_list.printLinkedList()


# def insertNodeAtPosition(head, data, position):
#     n = head
#     for _ in range(position - 1):
#         n = n.next
#         n_next = n.next
#     n.next = SinglyLinkedListNode(data)
#     n.next.next = n_next
#     return head

