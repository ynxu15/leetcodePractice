

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    def __repr__(self):
        return str(self.val)

    def __str__(self):
        return str(self.val)

class LinkedList:
    def __init__(self):
        self.head = self.Node(None)
        self.size = 0
        self.tail = self.head

    def add_first(self, e):
        new_node = self.Node(e)
        new_node.next = self.head.next
        self.head.next = new_node
        if self.size == 0:
            self.tail = new_node
        self.size += 1

    def add_last(self, e):
        new_node = self.Node(e)
        self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def add(self, index, element):
        self.check_position_index(index)
        if index == self.size:
            self.add_last(element)
            return

        prev = self.head
        for i in range(index):
            prev = prev.next
        new_node = Node(element)
        new_node.next = prev.next
        prev.next = new_node
        self.size += 1

    def remove_first(self):
        if self.is_empty():
            raise Exception("No Such Element")
        first = self.head.next
        self.head.next = first.next
        if self.size == 1:
            self.tail = self.head
        self.size -= 1
        return first.val

    def remove_last(self):
        if self.is_empty():
            raise Exception("no such element")

        prev = self.head
        while prev.next != self.tail:
            prev = prev.next
        val = self.tail.val
        prev.next = None
        self.tail = prev
        self.size -= 1
        return val

    def remove(self, index):
        self.check_element_index(index)

        prev = self.head
        for i in range(index):
            prev = prev.next
        val = prev.next.val
        prev.next = prev.next.next
        if index == self.size - 1:
            self.tail = prev
        self.size -= 1
        return val

    def get_first(self):
        if self.is_empty():
            raise Exception("NoSuchElementException")
        return self.head.next.val

    def get_last(self):
        if self.is_empty():
            raise Exception("NoSuchElementException")
        return self.get_node(self.size - 1).val

    def get(self, index):
        self.check_element_index(index)
        p = self.get_node(index)
        return p.val

    def set(self, index, element):
        self.check_element_index(index)
        p = self.get_node(index)

        old_val = p.val
        p.val = element

        return old_val

    # ***** 其他工具函数 *****
    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def is_element_index(self, index):
        return 0 <= index < self.size

    def is_position_index(self, index):
        return 0 <= index <= self.size

    # 检查 index 索引位置是否可以存在元素
    def check_element_index(self, index):
        if not self.is_element_index(index):
            raise IndexError(f"Index: {index}, Size: {self.size}")

    # 检查 index 索引位置是否可以添加元素
    def check_position_index(self, index):
        if not self.is_position_index(index):
            raise IndexError(f"Index: {index}, Size: {self.size}")

    # 返回 index 对应的 Node
    # 注意：请保证传入的 index 是合法的
    def get_node(self, index):
        p = self.head.next
        for i in range(index):
            p = p.next
        return p

    def find_node(self, value):
        curr = self.head
        while curr:
            if curr.data == value:
                return curr
        return None

    def insert_after(self, pre_node, value):
        if not pre_node:
            print("previous node is not in the list")
            return
        new_node = Node(value)
        new_node.next = pre_node.next
        pre_node.next = new_node

    def insert_before(self, post_node, value):
        if not post_node:
            print("post node is not in the list")
            return
        if self.head is None:
            print("list is empty")
            return
        if self.head == post_node:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
            return

        pre_node = self.head
        while pre_node.next is not None and pre_node.next != post_node:
            pre_node = pre_node.next
        if pre_node.next is None:
            print("post node is not in the list")
        new_node = Node(value)
        new_node.next = pre_node.next
        pre_node.next = new_node

    def remove1(self, value):
        curr = self.head
        if curr and curr.data == value:
            self.head = curr.next
        pre = None
        while curr and curr.data != value:
            pre = curr
            curr = curr.next
        if curr is None:
            return
        pre.next = curr.next
        curr = None
        return

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next
        last_node.next = new_node
        return

    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end='->')
            curr = curr.next
        print('None')


if __name__ == "__main__":
    list = LinkedList()
    list.add_first(1)
    list.add_first(2)
    list.add_last(3)
    list.add_last(4)
    list.add(2, 5)

    print(list.remove_first())  # 2
    print(list.remove_last())   # 4
    print(list.remove(1))       # 5

    print(list.get_first())     # 1
    print(list.get_last())      # 3
    print(list.get(1))          # 3