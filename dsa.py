
class StackList:
    def __init__(self):
        self.values = list()
        self.top = 0

    def push(self, item):
        self.values.append(item)
        self.top += 1
    
    def pop(self):
        temp = self.values[self.top]

        del self.values[-1]
        self.top -= 1

        return temp
    
    def peek(self):
        return self.values[top]

    def is_empty(self):
        return top == 0

    def size(self):
        return top + 1

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class StackLL:
    def __init__(self):
        self.size = 0
        self.head = None

    def push(self, value):
        newNode = Node(value)

        if self.head:
            newNode.next = self.head
        
        self.head = newNode
        self.size += 1
    
    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        
        poppedNode = self.head
        self.head = self.head.next
        self.size -= 1
        return poppedNode.value
    
    def peek(self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.head.value
    
    def isEmpty(self):
        return self.size == 0
    
    def stackSize(self):
        return self.size

    def traverseAndPrint(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.value, end =" -> ")
            currentNode = currentNode.next
        print()

class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue.pop(0)

    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue[0]

    def isEmpty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)