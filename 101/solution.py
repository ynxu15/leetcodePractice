# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def isSymmetric1(self, root: Optional[TreeNode]) -> bool:
        '''非递归方法'''
        if not root:
            return True
        # 层序遍历
        last_layer_queue = [root]
        curr_layer_queue = []
        flag = True
        while flag:
            # 判断是否对称
            len_queue = len(last_layer_queue)
            for i in range(len_queue >> 1):
                i_sym = len_queue - i - 1
                if last_layer_queue[i]:
                    if last_layer_queue[i_sym]:
                        if last_layer_queue[i].val != last_layer_queue[i_sym].val:
                            return False
                    else:
                        return False
                else:
                    if last_layer_queue[i_sym]:
                        return False

            # 获得下一层的队列
            flag = False
            for node in last_layer_queue:
                if node:
                    curr_layer_queue.append(node.left)
                    curr_layer_queue.append(node.right)
                    flag = True
                else:
                    curr_layer_queue.append(None)
                    curr_layer_queue.append(None)
            last_layer_queue, curr_layer_queue = curr_layer_queue, []
        return True
    def isSym(self, l_node, r_node):
        if not l_node and not r_node:
            return True
        if l_node and r_node and l_node.val == r_node.val and self.isSym(l_node.left, r_node.right) and self.isSym(l_node.right, r_node.left):
            return True
        return False
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        '''递归方法'''
        if not root:
            return True
        return self.isSym(root.left, root.right)
