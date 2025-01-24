

class Stack:
    def __init__(self):
        self.items = []
        self.size = 0

    def push(self, data):
        self.items.append(data)
        self.size += 1

    def pop(self):
        if self.size < 1:
            return None
        self.items.pop()
        self.size -=1

    def peek(self):
        if self.size > 0:
            return self.items[-1]

    def size(self):
        return self.size


