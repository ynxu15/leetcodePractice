from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k==1:
            return head

        def reverse(head, tail):
            new_head = None
            tail.next = None
            while head:
                pre, head = head, head.next
                pre.next = new_head
                new_head = pre

        pre_last = ListNode(0)
        new_head = pre_last
        pre_last.next = head
        fast, slow = head, head
        step = 1
        while fast:  # [slow, fast]  #之间的元素进行翻转
            if step == k:
                fast_next = fast.next
                reverse(slow, fast)
                pre_last.next = fast
                pre_last = slow
                slow, fast = fast_next, fast_next
                step = 1
            else:
                fast = fast.next
                step += 1

        if slow:
            pre_last.next = slow
        return new_head.next


if __name__ == '__main__':

    nums = [1,2,3,4,5]
    k = 2

    head = ListNode(0)
    p = head
    for n in nums:
        node = ListNode(n)
        p.next = node
        p = p.next

    p.next = None

    head = head.next

    solution = Solution()
    result = solution.reverseKGroup(head, k=2)
    print(result)
    pass
