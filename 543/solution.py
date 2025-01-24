# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def getDep(self, node):
        if not node:
            return -1, 0
        left_dep, left_long_link = self.getDep(node.left)
        right_dep, right_long_link = self.getDep(node.right)
        return max(left_dep, right_dep) + 1, max(left_dep + right_dep + 2, left_long_link,
                                                 right_long_link)  # 以当前节点为头的深度，和当前节点下的最长链路长度

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''树的深度'''
        dep, long_link = self.getDep(root)
        return long_link