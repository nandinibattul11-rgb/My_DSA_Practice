class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
    
class stack:
    def __init__(self):
        self.top = None
        
    def isempty(self):
        return self.top is None
    def push(self,new_node):
        new_node.next = self.top
        self.top = new_node
        
    def reverse_string(self, string):
        temp = []
        for ch in string:
            temp.append(ch)
        reverse = ""
        while len(temp) > 0:
            reverse += temp.pop()
        print("Reversed String:", reverse)
            
    def print(self):
        if self.isempty():
            print("Stack is Empty")
        else:
            print("Stack Contents....")
            temp = self.top
            while temp:
                print(temp.data)
                temp=temp.next
            
st = stack()

st.push(Node(1))
st.push(Node(2))
st.push(Node(3))
st.push(Node(4))
st.push(Node(5))
st.reverse_string("NANDINI")
st.print()
        