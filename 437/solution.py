from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum2(self, root: Optional[TreeNode], targetSum: int) -> int:
        '''错误的，没有通过所有实例'''

        def checkTree(root, targetSum, requires):
            if not root:
                if 0 in requires:
                    return 0, {0:0}
                return 0, {}
            requires1 = [r-root.val for r in requires]
            requires1.append(targetSum-root.val)
            count1, map1 = checkTree(root.left, targetSum, requires1)
            count2, map2 = checkTree(root.right, targetSum, requires1)
            for r in map1:
                if r in map2:
                    map2[r] += map1[r]
                else:
                    map2[r] = map1[r]

            count = 0
            if targetSum - root.val in map2:
                count = map2[targetSum-root.val]
                if count == 0:
                    count = 1

            map = {}
            for r in map2:
                r1 = r+root.val
                if r1 in requires:
                    map[r1] = map2[r]

            if root.val not in map:
                map[root.val] = 1
            else:
                map[root.val] += 1

            # count = 0
            # if targetSum in map:
            #     count = map[targetSum]

            return count1+count2+count, map

        count, map = checkTree(root, targetSum, [])
        return count

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        import collections
        prefix = collections.defaultdict(int)
        prefix[0] = 1

        def dfs(root, curr):
            if not root:
                return 0

            ret = 0
            curr += root.val
            ret += prefix[curr - targetSum]
            prefix[curr] += 1
            ret += dfs(root.left, curr)
            ret += dfs(root.right, curr)
            prefix[curr] -= 1

            return ret

        return dfs(root, 0)

if __name__ == '__main__':

    root = TreeNode(1)


    # root = TreeNode(10)
    # root.left = TreeNode(5)
    # root.left.left = TreeNode(3)
    # root.left.left.left = TreeNode(3)
    # root.left.left.right = TreeNode(-2)
    # root.left.right = TreeNode(2)
    # root.left.right.right = TreeNode(1)
    # root.right = TreeNode(-3)
    # root.right.right = TreeNode(11)

    print(Solution().pathSum(root, 1))