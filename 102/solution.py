# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        last_queue = [root]
        curr_queue = []
        ans = []
        while last_queue:
            for node in last_queue:
                if node.left:
                    curr_queue.append(node.left)
                if node.right:
                    curr_queue.append(node.right)
            ans.append([n.val for n in last_queue])
            last_queue, curr_queue = curr_queue, []

        return ans