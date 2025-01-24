# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validBST(node, min_val, max_val):
            if not node:
                return True
            if node.val <= min_val or node.val >= max_val:
                return False

            if node.left and node.left.val >= node.val:
                return False
            if node.right and node.right.val <= node.val:
                return False
            return validBST(node.left, min_val, node.val) and validBST(node.right, node.val, max_val)

        return validBST(root, -2 ** 31 - 1, 2 ** 31 + 1)