from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head

        h = ListNode(-1)

        h.next, fast, slow = head, h, h
        for i in range(n):
            if fast.next:
                fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return h.next



if __name__ == '__main__':


    # solution = Solution()
    # result = solution.exist(board, word)
    # print(result)
    pass
