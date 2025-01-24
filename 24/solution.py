from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        h = ListNode(0)
        h.next = head
        pre, fast, slow = h, h, h
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast:
                slow.next = fast.next
                fast.next = slow
                pre.next = fast
                pre = slow
                fast = slow
        return h.next

if __name__ == '__main__':


    # solution = Solution()
    # result = solution.exist(board, word)
    # print(result)
    pass
