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
    
    def identical(self, q2):
        temp1 = self.front
        temp2 = q2.front

        while temp1 and temp2:
            if temp1.data != temp2.data:
                print("Queues are Not Identical")
                return

            temp1 = temp1.next
            temp2 = temp2.next

        if temp1 is None and temp2 is None:
            print("Queues are Identical")
        else:
            print("Queues are Not Identical")
                    
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
q2 = queue()
q1.enqueue(Node(21))
q1.enqueue(Node(22))
q1.enqueue(Node(23))
q1.enqueue(Node(24))

q1.display()
q2.enqueue(Node(50))
q2.enqueue(Node(60))
q2.enqueue(Node(70))
q2.display()
q1.identical(q2)