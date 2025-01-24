'''
设计一个有getMin 功能的栈
'''

class Stack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def pop(self):
        if not self.stack:
            raise Exception("栈为空")
        item = self.stack.pop()
        if self.minStack and item == self.minStack[-1]:
            self.minStack.pop()
        return item

    def push(self, value):
        self.stack.append(value)
        if not self.minStack or value <= self.minStack[-1]:
            self.minStack.append(value)
    def getMin(self):
        if not self.stack:
            return None
        if not self.minStack:
            return self.stack[-1]