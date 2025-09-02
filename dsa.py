
class Stack:
    def __init__(self):
        self.values = list()
        self.top = 0

    def push(self, item):
        self.values.append(item)
        self.top += 1
    
    def pop(self):
        
        temp = self.values[self.top]

        del self.values[-1]
        self.top -= 0

        return temp
    
    def peek(self):
        return self.values[top]

    def is_empty(self):
        return top == 0

    def size(self):
        return top + 1