from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        # 前序
        def build(pre_left, pre_right, inorder_left, inorder_right):
            if pre_left > pre_right:
                return None
            if pre_left == pre_right:
                return TreeNode(preorder[pre_left])
            head = TreeNode(preorder[pre_left])
            index = inorder.index(head.val)

            left_count = index - inorder_left
            head.left = build(pre_left+1, pre_left+left_count, inorder_left, index-1)
            head.right = build(pre_left + left_count + 1, pre_right, index + 1, inorder_right)
            return head

        return build(0, len(preorder)-1, 0, len(preorder)-1)



if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]

    # preorder = [-1]
    # inorder = [-1]

    preorder = [1, 2]
    inorder = [1, 2]

    preorder = [3, 1, 2, 4]
    inorder = [1, 2, 3, 4]


    Solution().buildTree(preorder, inorder)