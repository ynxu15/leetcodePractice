from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def search(node, k):
            if not node:
                return -1, k
            r, k1 = search(node.left, k)
            if r >= 0:
                return r, 0
            else:
                if k1 == 1:
                    return node.val, 0
                r, k2 = search(node.right, k1-1)
                return r, k2
        r, k1 = search(root, k)
        if r >= 0:
            return r
        return -1

if __name__ == '__main__':

    root = TreeNode(3)
    node = TreeNode(1)
    root.left = node
    node = TreeNode(2)
    root.left.right = node
    node.right = TreeNode(4)

    Solution().kthSmallest(root, 1)