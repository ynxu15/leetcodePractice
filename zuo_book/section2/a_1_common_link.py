'''
打印两个有序链表的公共部分
'''

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


head1 = None
head2 = None

def print_common_link(head1, head2):
    if not head1 or not head2:
        return

    while head1 is not None and head2 is not None:
        if head1.data == head2.data:
            print(head1.data, end=" ")
            head1 = head1.next
            head2 = head2.next
        else:
            if head1.data <= head2.data:
                head1 = head1.next
            else:
                head2 = head2.next
