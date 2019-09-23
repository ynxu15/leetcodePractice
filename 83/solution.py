#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        fastP, slowP = head, head
        while fastP != None:
            if slowP.val != fastP.val and slowP != fastP:
                slowP.next = fastP
                slowP, fastP =fastP, fastP.next
            else:
                fastP = fastP.next
        slowP.next = None
        return head

def buildLink(numList = [1,1,1,3,4,4,5]):
    head = ListNode(0)
    p = head
    for n in numList:
        p.next = ListNode(n)
        p = p.next
    return head.next

def printLink(head):
    p = head
    while p != None:
        print(p.val, '', end='')
        p = p.next
    print('')

if __name__ == "__main__":
    head = buildLink(numList = [1,1])
    printLink(Solution().deleteDuplicates(head))