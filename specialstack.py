class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.minimun = None
        self.top = None
        self.count = 0

    def push(self, value):
        if self.top is None:
            self.top = Node(value)
            self.minimum = value
        elif value<self.minimum:
            temp = (2*value) - self.minimum
            new_node = Node(temp)
            new_node.next = self.top
            self.top = new_node
            self.minimun = value
        else:
            new_node = Node(value)
            new_node.next = self.top
            self.top = new_node
        print("Number Inserted: {}" .format(value))

    def pop(self):
        if self.top is None: 
            print( "Stack is empty") 
        else:
            removedNode = self.top.value
            self.top = self.top.next
            if removedNode < self.minimum:
                print("Number removed: {}" .format(self.minimum))
                self.minimum = ( ( 2 * self.minimum ) - removedNode )
            else:
                print("Number removed: {}" .format(removedNodee))
    
    def isEmpty(self):
        if self.top is None:
            return True
        else:
            return False
    
    def peek(self):
        if self.top is None:
            print('the stack is empty')
        else:
            if self.top.value<self.minimum:
                print("top most value is",self.minimum) 
            else:
                return print("top most value is",self.top.value)
    

    def getMin(self): 
        if self.top is None: 
            return "Stack is empty"
        else: 
            print("Minimum Element in the stack is: {}" .format(self.minimum)) 


stack = Stack()  
stack.push(3) 
stack.push(5)  
stack.getMin() 
stack.push(2) 
stack.push(1) 
stack.getMin()      
stack.pop() 
stack.getMin() 
stack.pop()  
stack.peek()

    
