class Node:
    def __init__(self,value):
        self.left = None
        self.data = value
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self,new_node):
        if self.root is None:  # creating the Root Node
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

                else:
                    if temp.right is None:
                        temp.right = new_node
                        return
                    else:
                        temp = temp.right

    def search_node(self,temp,val):
        if temp is None:
            return False

        if val == temp.data:
            return True

        elif val < temp.data:
            return self.search_node(temp.left,val)

        else:
            return self.search_node(temp.right,val)

    def inorder(self,temp):  # recursive
        if temp is None:
            return
        else:
            self.inorder(temp.left)
            print(temp.data,end=" ")
            self.inorder(temp.right)

# Creating BST
btree = BST()

btree.insert(Node(11))
btree.insert(Node(5))
btree.insert(Node(13))
btree.insert(Node(16))
btree.insert(Node(2))
btree.insert(Node(40))

# Inorder Traversal
print("Inorder Traversal:")
btree.inorder(btree.root)
# Searching Node
val = 13
print("\n\nSearching Node:",val)
if btree.search_node(btree.root,val):
    print("The Given Node Exists")
else:
    print("The Given Node Does Not Exists")