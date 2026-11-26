# Binary Search Tree

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

    def del_node(self,root,val):
        if root is None:
            return

        if val < root.data:
            root.left = self.del_node(root.left,val)

        elif val > root.data:
            root.right = self.del_node(root.right,val)

        else:
            if root.left is None:  # Node with Right Child Only
                return root.right

            if root.right is None:  # Node with Left Child Only
                return root.left

            # Node has both left and right child
            succ = self.get_successor(root)
            root.data = succ.data
            root.right = self.del_node(root.right,succ.data)

        return root

    def get_successor(self,temp):
        temp = temp.right

        while temp.left is not None:
            temp = temp.left

        return temp

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


# Displaying BST Before Deletion
print("Before Deletion:")
btree.inorder(btree.root)


# Deleting Node
val = 13
print("\n\nDeleting Node:",val)

btree.root = btree.del_node(btree.root,val)

# Displaying BST After Deletion
print("\nAfter Deletion:")
btree.inorder(btree.root)

print()