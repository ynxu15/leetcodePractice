# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''层序遍历，每一层返回最右侧的节点'''
        if not root:
            return []
        last_queue = [root]
        curr_queue = []
        ans = []
        while last_queue:
            ans.append(last_queue[-1].val)
            for node in last_queue:
                if node.left:
                    curr_queue.append(node.left)
                if node.right:
                    curr_queue.append(node.right)
            last_queue, curr_queue = curr_queue, []
        return ans