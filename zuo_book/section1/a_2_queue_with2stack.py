'''
两个栈实现队列
'''

class QueueWith2Stack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def add(self, value):
        self.stack1.append(value)

    def poll(self):
        if not self.stack1:
            raise Exception("the queue is empty")
        while self.stack1:
            item = self.stack1.pop()
            self.stack2.append(item)
        target = self.stack2.pop()
        while self.stack2:
            item = self.stack2.pop()
            self.stack1.append(item)
        return target

    def peek(self):
        if not self.stack1:
            raise Exception("the queue is empty")
        while self.stack1:
            item = self.stack1.pop()
            self.stack2.append(item)
        target = self.stack2[-1]
        while self.stack2:
            item = self.stack2.pop()
            self.stack1.append(item)
        return target