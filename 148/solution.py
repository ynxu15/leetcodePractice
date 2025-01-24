from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        p = head
        nodes = []
        while p:
            nodes.append(p)
            p = p.next
        nodes = sorted(nodes, key=lambda x: x.val)
        head = nodes[0]
        p = head
        for n in nodes[1:]:
            p.next = n
            p = p.next
        p.next = None
        return head

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head  # termination.
        # cut the LinkedList at the mid index.
        slow, fast = head, head.next
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        mid, slow.next = slow.next, None  # save and cut.
        # recursive for cutting.
        left, right = self.sortList(head), self.sortList(mid)
        # merge `left` and `right` linked list and return it.
        h = res = ListNode(0)
        while left and right:
            if left.val < right.val:
                h.next, left = left, left.next
            else:
                h.next, right = right, right.next
            h = h.next
        h.next = left if left else right
        return res.next

if __name__ == '__main__':
    pass



