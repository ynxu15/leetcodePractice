class DyArrayList:
    # 默认初始化容量
    INIT_CAP = 1

    def __init__(self, init_capacity=None):
        self.data = [None] * (init_capacity if init_capacity is not None else self.__class__.INIT_CAP)
        self.size = 0
        self.capacity = len(self.data)

    def add_last(self, e):
        if self.size == self.capacity:
            self._resize(2*self.capacity)
        self.data[self.size] = e
        self.size += 1

    def add(self, index, e):
        if self.size == self.capacity:
            self._resize(2*self.capacity)
        for i in range(self.size-1, index-1, -1):
            self.data[i+1] = self.data[i]

        self.data[index] = e
        self.size += 1

    def add_first(self, e):
        self.add(0, e)

    def remove_last(self):
        if self.size == 0:
            raise Exception("数据表为空")
        if self.size == self.capacity // 4:
            self._resize(self.capacity//2)

        deleted_val = self.data[self.size-1]
        self.data[self.size-1] = None
        self.size -= 1
        return deleted_val

    def remove(self, index):
        self._check_element_index(index)
        if self.size == self.capacity//4:
            self._resize(self.capacity//2)
        deleted_val = self.data[index]
        for i in range(index+1, self.size):
            self.data[i-1] = self.data[i]
        self.data[self.size-1] = None
        self.size -= 1
        return deleted_val

    def remove_first(self):
        return self.remove(0)

    def get(self, index):
        self._check_element_index(index)
        return self.data[index]

    def set(self, index, element):
        self._check_element_index(index)
        old_val = self.data[index]
        self.data[index] = element
        return old_val

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def _resize(self, new_cap):
        temp = [None] * new_cap
        for i in range(self.size):
            temp[i] = self.data[i]
        self.capacity = new_cap
        self.data = temp

    def _is_element_index(self, index):
        return 0<=index<self.size

    def _is_position_index(self, index):
        return 0<=index<=self.size

    def _check_element_index(self, index):
        if not self._is_element_index(index):
            raise IndexError(f"Index: {index}, Size: {self.size}")

    def _check_position_index(self, index):
        if not self._is_position_index(index):
            raise IndexError(f"Index: {index}, Size: {self.size}")

    def display(self):
        print(f"size={self.size}, cap={self.capacity}")
        print(self.data)

# Usage example
if __name__ == "__main__":
    arr = DyArrayList(init_capacity=3)

    # 添加 5 个元素
    for i in range(1, 6):
        arr.add_last(i)

    arr.remove(3)
    arr.add(1, 9)
    arr.add_first(100)
    val = arr.remove_last()

    # 100 1 9 2 3
    for i in range(arr.size):
        print(arr.get(i))