class Node:
    def __init__(self,data=None):
        self.right = None
        self.left = None
        self.value = data

def insertNode(root,node):
    if node == Node:
        node = root
    else:
        if node.value <= root.value:
            # left
            if root.left is None:
                insertNode(root.left, node)

        else:
            #right
            print("hello")
