# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.invert(root)
        return root

    def invert(self, node):
        if not node:
            return node
        node.left, node.right = node.right, node.left
        self.invert(node.left)
        self.invert(node.right)