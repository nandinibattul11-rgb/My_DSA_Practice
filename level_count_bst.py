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
                            
    def inorder(self,temp): #recursive
        if temp is None:
            return
        else:
            self.inorder(temp.left)
            print(temp.data,end = " ")
            self.inorder(temp.right)
            
    def level_order(self,root):
        if root is None:
            print("BST is Empty")
            return
        arr=[]
        cnt = 0
        level = 0
        arr.append(root)
        while cnt <len(arr):
            node_count = len(arr) - cnt
            print("\nLevel: ",level,end=" ")
            for i in range(node_count):
                temp = arr[cnt]
                cnt += 1
                print(temp.data,end=" ")
                if temp.left:
                    arr.append(temp.left)
                if temp.right:
                    arr.append(temp.right)
            level += 1
        print("\nHeight of the Tree: ",level-1)
btree = BST()
btree.insert(Node(11))
btree.insert(Node(5))
btree.insert(Node(13))
btree.insert(Node(16))
btree.insert(Node(2))
btree.insert(Node(40))
print("Inorder: ")
btree.inorder(btree.root)
print("\nLevel Order: ")
btree.level_order(btree.root)
