# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional
class Solution:
    def getDepth(self, node):
        if not node:
            return 0
        return max(self.getDepth(node.left), self.getDepth(node.right)) + 1

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.getDepth(root)