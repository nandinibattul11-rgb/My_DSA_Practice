#Binary Search Tree
class Node:
    def __init__(self,value):
        self.left = None
        self.data = value
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    def insert(self,new_node):
        if self.root is None: #creating the Root Node
            self.root = new_node
            return
        else:
            temp = self.root
            while True:
                if new_node.data < temp.data:
                    if temp.left is None:
                        temp.left = new_node                            
                        return
                    else:
                        temp = temp.left
                elif new_node.data >= temp.data:
                    if temp.right is None:
                        temp.right = new_node
                        return
                    else:
                        temp = temp.right
                            
def postorder(temp): #recursive
    if temp is None:
        return
    else:
        postorder(temp.left)
        postorder(temp.right)
        print(temp.data,end = " ")
        
btree = BST()
btree.insert(Node(11))
btree.insert(Node(5))
btree.insert(Node(13))
btree.insert(Node(16))
btree.insert(Node(2))
btree.insert(Node(40))
postorder(btree.root)