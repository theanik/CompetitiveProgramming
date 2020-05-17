class Node:
    def __init__(self, data):
        self.data = data
        self.nextAddress = None

class LinkedList:
    def __init__(self):
        self.hade = None 

        
    # def printList(self):
    #     tmp = self.hade
    #     while(tmp != None):
    #         print(tmp.data)
    #         tmp = tmp.nextAddress
    
    # recursive way
    def printListRecursive(self,hade):
        if hade is not None:
            print(hade.data)
            self.printListRecursive(hade.nextAddress)
    
linked_list = LinkedList()

linked_list.hade = Node("Anik")
second = Node("Shakil")
third = Node("Sahidul")
four = Node("Niloy")
linked_list.hade.nextAddress = second
second.nextAddress = third


# linked_list.printList()
linked_list.printListRecursive(linked_list.hade)
