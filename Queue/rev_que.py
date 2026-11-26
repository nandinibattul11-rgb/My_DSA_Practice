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
    
    def reverse_queue(self):
        if self.front is None:
            print("Queue is Empty")
        else:
            temp_stack = []
            temp = self.front

            while temp:
                temp_stack.append(temp.data)
                temp = temp.next

            self.front = None
            self.rear = None

            while len(temp_stack) > 0:
                self.enqueue(Node(temp_stack.pop()))

            print("Reversed Queue:")
            self.display()

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
q1.reverse_queue()
