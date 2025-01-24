from typing import List


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = {}
        self.queue = []

    def get(self, key: int) -> int:
        if key in self.data:
            self.queue.remove(key)
            self.queue.insert(0, key)
            return self.data[key]
        else:
            return -1
    def put(self, key: int, value: int) -> None:
        if key in self.data:
            self.queue.remove(key)
            self.queue.insert(0, key)
            self.data[key] = value
        else:
            if len(self.queue) == self.capacity:
                k = self.queue.pop()
                del self.data[k]
                self.queue.insert(0, key)
                self.data[key] = value
            else:
                self.queue.insert(0, key)
                self.data[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == '__main__':
    # 输入
    # ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    # [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    # 输出
    # [null, null, null, 1, null, -1, null, -1, 3, 4]
    #
    solution = LRUCache(2)
    print(solution.put(1,1))
    print(solution.put(2, 2))
    print(solution.get(1))
    print(solution.put(3, 3))
    print(solution.get(2))
    print(solution.put(4, 4))
    print(solution.get(1))
    print(solution.get(3))
    print(solution.get(4))


