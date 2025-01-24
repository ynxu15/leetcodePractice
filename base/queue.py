
'''
从list的尾部插入，从头部删除
'''
class ListQueue:
    def __init__(self):
        self.queue = []
        self.size = 0

    def enqueue(self, value):
        self.queue.append(value)
        self.size += 1

    def dequeue(self):
        data = self.queue.pop(0)
        self.size -= 1
        return data


'''
从list的头部插入，从尾部删除
'''
class ListQueue1:
    def __init__(self):
        self.queue = []
        self.size = 0

    def enqueue(self, value):
        self.queue.insert(0, value)
        self.size += 1

    def dequeue(self):
        if self.size < 1:
            return None
        data = self.queue.pop()
        self.size -= 1
        return data

'''
使用数组实现
'''
class ListQueue2:
    def __init__(self):
        self.queue = []
        self.size = 0
        self.head_index = 0
        self.tail_index = 0
    def enqueue(self, value):
        self.queue.append(value)
        self.size += 1
        self.tail_index += 1

    def dequeue(self):
        if self.size < 1:
            return None
        data = self.queue[self.head_index]
        self.size -= 1
        self.head_index += 1
        return data