
'''
利用前缀和，找到最小的前缀和  最大的前缀和， 两者之差就是要求的最大子数组
'''
class Solution:
    def maxSubArray(self, nums) -> int:
        if not nums:
            return 0

        min_acc_sum = 0
        acc_sum = 0
        max_arr_sum = -10**5
        for n in nums:
            acc_sum += n
            if acc_sum - min_acc_sum > max_arr_sum:
                max_arr_sum = acc_sum - min_acc_sum
            if acc_sum < min_acc_sum:
                min_acc_sum = acc_sum
        return max_arr_sum


if __name__ == '__main__':
    #nums = [-2,1,-3,4,-1,2,1,-5,4] # 输出6
    #nums = [1] # 1
    #nums = [5, 4, -1, 7, 8] # 23
    nums = [-1] # -1


    solution = Solution()
    print(solution.maxSubArray(nums))