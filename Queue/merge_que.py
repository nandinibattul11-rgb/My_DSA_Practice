class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, new_node):
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
            
    def merge(self, q2):
        merged = queue()
        temp = self.front
        while temp:
            merged.enqueue(Node(temp.data))
            temp = temp.next
        temp = q2.front
        while temp:
            merged.enqueue(Node(temp.data))
            temp = temp.next
        print("Merged Queue:")
        merged.display()
        return merged 
           
    def display(self):
        if self.front is None:
            print("Queue is Empty")
        else:
            print("Queue Contents....")
            temp = self.front
            while temp:
                print(temp.data)
                temp = temp.next
                
q1 = queue()
q1.enqueue(Node(21))
q1.enqueue(Node(22))
q1.enqueue(Node(23))
q1.enqueue(Node(24))
q1.display()
q2 = queue()

q2.enqueue(Node(50))
q2.enqueue(Node(60))
q2.enqueue(Node(70))
q2.display()
q3 = q1.merge(q2)