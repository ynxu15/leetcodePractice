from typing import List
class Solution:
    def trans(self, nums, l, r):
        if l > r:
            return None
        mid = (l+r) >> 1
        node = TreeNode(val=nums[mid])
        node.left = self.trans(nums, l, mid-1)
        node.right = self.trans(nums, mid+1, r)
        return node

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        return self.trans(nums, 0, len(nums)-1)

