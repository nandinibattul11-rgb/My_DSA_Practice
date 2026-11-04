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
        
    def pop(self):
        if self.isempty():
            print("Stack is Empty")
        else:
            temp = self.top
            print("Popped Element: ",temp.data)
            self.top = self.top.next
            temp = None
            
    def display(self):
        if self.isempty():
            print("Stack is Empty")
        else:
            print("Stack Contents....")
            temp = self.top
            while temp:
                print(temp.data)
                temp=temp.next
            
st = stack()

st.push(Node(11))
st.push(Node(22))
st.push(Node(33))
st.push(Node(44))
st.pop()
st.pop()
st.display()
        
        
