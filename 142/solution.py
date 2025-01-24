from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def print_link(head):
            index = 0
            while head:
                index += 1
                if index > 10:
                    break
                print(head.val, ' -> ', end='')
                head = head.next
            print()
        print_link(head)

        fast, slow = head, head
        while True:
            if fast and fast.next:
                fast = fast.next.next
            else:
                return -1
            slow = slow.next
            if fast == slow:
                break
        index = 0
        fast = head
        while fast != slow:
            fast = fast.next.next
            slow = slow.next
            index += 1
            if fast == slow:
                break
        return fast


if __name__ == '__main__':
    head = [3, 2, 0, -4]
    pos = 1

    h = ListNode(head[0])
    t = None
    pre_= h
    for index, n in enumerate(head):
        if index == 0:
            continue
        node = ListNode(n)
        pre_.next = node
        pre_ = pre_.next
        if pos == index:
            t = node
    if pos == 0:
        t = head
    pre_.next = t

    solution = Solution()
    result = solution.detectCycle(h)
    print(result)

