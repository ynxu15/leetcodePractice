class Solution:
    def maxSubArray(self, nums) -> int:
        if len(nums)<1:
            return 0
        sumResult = [0]*len(nums)
        sumResult[0], maxNum = nums[0], nums[0]
        for i in range(1,len(nums)):
            sumResult[i] = max(sumResult[i-1]+nums[i], nums[i])
            if sumResult[i] > maxNum:
                maxNum = sumResult[i]
        return maxNum


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))