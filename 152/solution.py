from typing import List
class Solution:
    def maxProduct1(self, nums: List[int]) -> int:
        if not nums:
            return 0

        preDp = [0, 0, 1, 1] # 包含自身的最大正乘积， 不包含自身的最大正乘积， 包含自身的最小负乘积，不包含自身的最小负数乘积
        positive_count = 0
        # if nums[0] >= 0:
        #     preDp = [nums[0], 0, 1, 1]
        #     positive_count += 1
        # else:
        #     preDp = [-1, -1, nums[0], 0]
        currDp = [0]*4
        for n in nums:
            if n >= 0:
                positive_count += 1
            #p0, p1, p2, p3
            p1, p2 = preDp[0]*n, preDp[2]*n
            currDp[0] = max(p1, n, p2)
            currDp[1] = max(preDp[0], preDp[1])
            currDp[2] = min(p1, n, p2)
            currDp[3] = min(preDp[2], preDp[3])
            if currDp[2] > 0:
                currDp[2] = 1
            if currDp[3] > 0:
                currDp[3] = 1
            preDp = currDp
            currDp = [0]*4
        if positive_count > 0:
            return max(preDp[0], preDp[1])
        else:
            if preDp[0] > 0 or preDp[1] > 0:
                return max(preDp[0], preDp[1])
            if preDp[2] < 0:
                if preDp[3] < 0:
                    return max(preDp[2], preDp[3])
                else:
                    return preDp[2]
            else:
                return preDp[3]

    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        preDp = [1, 1]  # 包含自身的最大正乘积， 包含自身的最小乘积
        currDp = [0, 0]
        ans = []
        for n in nums:
            p1, p2 = preDp[0]*n, preDp[1]*n
            currDp[0] = max(p1, p2, n)
            currDp[1] = min(p1, p2, n)
            preDp = currDp
            currDp = [0, 0]
            ans.append(preDp[0])
        return max(ans)



if __name__ == '__main__':
    # nums = [-1, -2]
    # nums = [-1]

    nums = [2, 3, -2, 4]
    # 输出: 6
    # 解释: 子数组[2, 3]有最大乘积6。

    # nums = [-2, 0, -1]
    # # 输出: 0
    # # 解释: 结果不能为 2, 因为[-2, -1] 不是子数组。

    solution = Solution()
    result = solution.maxProduct(nums)
    print(result)