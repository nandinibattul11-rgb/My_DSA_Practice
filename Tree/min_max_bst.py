#Binary Search Tree
class Node:
    def __init__(self,value):
        self.left = None
        self.data = value
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        self.lcnt = 0
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
                            
    def inorder(self, temp): #recursive
        if temp is None:
            return
        else:
            self.inorder(temp.left)
            print(temp.data,end = " ")
            if temp.left is None and temp.right is None:
                self.lcnt += 1
            self.inorder(temp.right)
            
    def find_minmax(self,temp):
        temp = self.root
        while temp.left:
            temp = temp.left
        print("\nMin Value: ",temp.data)
        temp = self.root
        while temp.right:
            temp = temp.right
        print("Max Value: ",temp.data)
btree = BST()
btree.insert(Node(11))
btree.insert(Node(1))
btree.insert(Node(5))
btree.insert(Node(13))
btree.insert(Node(16))
btree.insert(Node(19))
btree.insert(Node(2))
btree.insert(Node(40))
btree.inorder(btree.root)
print("\n Total Leaf Nodes: ",btree.lcnt)
btree.find_minmax(btree.root)