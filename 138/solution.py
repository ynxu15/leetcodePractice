from typing import List

"""
# Definition for a Node.
"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        oldNewMap = {}
        h2 = Node(head.val)
        p1, p2 = head, h2
        oldNewMap[p1] = p2
        while p1.next:
            n = Node(p1.next.val)
            p2.next = n
            oldNewMap[p1.next] = p2.next
            p1, p2 = p1.next, p2.next
        p2.next = None

        p1, p2 = head, h2
        while p1:
            rand1 = p1.random
            if rand1:
                rand2 = oldNewMap[rand1]
                p2.random = rand2
            else:
                p2.random = None
            p1, p2 = p1.next, p2.next

        return h2

        def copyRandomList2(self, head: 'Optional[Node]') -> 'Optional[Node]':
            '''新生成的节点，挂在原节点的后面，那random就好处理了，新的random是原来random.next'''
            if head is None:
                return None

            # 复制每个节点，把新节点直接插到原节点的后面
            cur = head
            while cur:
                cur.next = Node(cur.val, cur.next)
                cur = cur.next.next

            # 遍历交错链表中的原链表节点
            cur = head
            while cur:
                if cur.random:
                    # 要复制的 random 是 cur.random 的下一个节点
                    cur.next.random = cur.random.next
                cur = cur.next.next

            # 遍历交错链表中的新链表节点
            cur = head.next
            while cur.next:
                # 删除原链表的节点，即当前节点的下一个节点
                cur.next = cur.next.next
                cur = cur.next

            # 返回 head.next 就相当于删除了原链表的头节点
            return head.next

if __name__ == '__main__':


    # solution = Solution()
    # result = solution.exist(board, word)
    # print(result)
    pass
