
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.next = self.head
        self.size = 0

    def add_last(self, e):
        x = Node(e)
        temp = self.tail.prev
        temp.next = x
        x.prev = temp

        x.next = self.tail
        self.tail.prev = x
        self.size += 1

    def add_first(self, e):
        x = Node(e)
        temp = self.head.next
        temp.prev = x
        x.next = temp

        self.head.next = x
        x.prev = self.head
        self.size += 1

    def add(self, index, element):
        self.check_position_index(index)
        if index == self.size:
            self.add_last(element)
            return

        p = self.get_node(index)
        temp = p.prev

        x = Node(element)
        p.prev = x
        temp.next = x
        x.prev = temp
        x.next = p

        self.size += 1

    def remove_first(self):
        if self.size < 1:
            raise IndexError("No elements to remove")
        x = self.head.next
        temp = x.next
        self.head.next = temp
        temp.prev = self.head
        self.size -= 1
        return x.val

    def remove_last(self):
        if self.size < 1:
            raise IndexError("No elements to remove")
        x = self.tail.prev
        temp = x.prev
        self.tail.prev = temp
        temp.next = self.tail

        self.size -= 1
        return x.val

    def remove(self, index):
        self.check_element_index(index)
        x = self.get_node(index)
        prev = x.prev
        next = x.next
        prev.next = next
        next.prev = prev
        self.size -= 1
        return x.val

    def get(self, index):
        self.check_element_index(index)
        p = self.get_node(index)
        return p.val

    def get_first(self):
        if self.size < 1:
            raise IndexError("No elements in the list")

        return self.head.next.val

    def get_last(self):
        if self.size < 1:
            raise IndexError("No elements in the list")
        return self.tail.prev.val

    def set(self, index, val):
        self.check_element_index(index)
        p = self.get_node(index)
        old_val = p.val
        p.val = val
        return old_val

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def get_node(self, index):
        self.check_element_index(index)
        p = self.head.next
        for _ in range(index):
            p = p.next
        return p

    def is_element_index(self, index):
        return 0 <= index < self.size

    def is_position_index(self, index):
        return 0 <= index <= self.size

    def check_element_idnex(self, index):
        if not self.is_element_index(index):
            raise IndexError(f"Index: {index}, Size:{self.size}")

    def check_position_index(self, index):
        if not self.is_position_index(index):
            raise IndexError(f"Index: {index}, Size:{self.size}")

    def display(self):
        print(f"size = {self.size}")
        p = self.head.next
        while p != self.tail:
            print(f"{p.val} <-> ", end="")
            p = p.next
        print("null\n")

if __name__ == "__main__":
    list = DoubleLinkedList()
    list.add_last(1)
    list.add_last(2)
    list.add_last(3)
    list.add_first(0)
    list.add(2, 100)

    list.display()
    # size = 5
    # 0 <-> 1 <-> 100 <-> 2 <-> 3 <-> null



