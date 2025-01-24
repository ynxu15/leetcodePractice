

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.pre = None

head1 = None
k = 5

# 单链表删除
def del_last_k_node(head1, k):
    if not head1:
        raise Exception("the list is empty")
    if k <= 0:
        raise Exception("bad params k")
    # 找到第K个
    fast_p, slow_p = head1, head1
    for i in range(k):
        if fast_p.next == None:
            raise Exception("the list does not have more than k elements")
        fast_p = fast_p.next
    while fast_p.next != None:
        fast_p = fast_p.next
        slow_p = slow_p.next
        



# 双链表删除
def del_last_k_node1(head1, k):
    pass