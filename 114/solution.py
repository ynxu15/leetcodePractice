from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """


        if not root:
            return None

        self.flatten(root.left)
        self.flatten(root.right)
        left, right = root.left, root.right
        root.left = None
        root.right = left
        p1 = left
        while p1 and p1.right:
            p1 = p1.right
        if p1:
            p1.right = right
        else:
            root.right = right
        return root


if __name__ == '__main__':

    root = TreeNode(1)
    node = TreeNode(2)
    root.left = node
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right = TreeNode(5)
    root.right.right = TreeNode(6)

    Solution().flatten(root)