from typing import List

class Solution:
    def findDuplicate2(self, nums: List[int]) -> int:
        t = 0
        for n in nums:
            if t >> n & 1 == 1:
                return n
            t |= 1 << n
        return None

    def findDuplicate3(self, nums: List[int]) -> int:
        '''自定义位图'''
        # 一个数是32位，
        # 10^5+1需要 313个数
        bitmap = [0]*313
        t = 0
        for n in nums:
            index1 = n // 32
            left_num = n - index1*32
            if bitmap[index1] >> left_num & 1 == 1:
                return n
            bitmap[index1] |= 1 << left_num
        return None

    def findDuplicate(self, nums: List[int]) -> int:
        '''二分查找'''
        # 先排序，然后二分法，找index和数对不上的位置。 正常应该是nums[i] = i + 1
        nums = sorted(nums)
        l, r = 0, len(nums)-1
        nums_len = len(nums)
        def check(l, r, nums):
            while l < r:
                mid = (l+r)//2
                if nums[mid] > mid + 1:
                    l = mid + 1
                elif nums[mid] < mid + 1:
                    r = mid - 1
                else:
                    result = check(l, mid-1, nums)
                    if result > 0:
                        return result
                    result = check(mid+1, r, nums)
                    if result > 0:
                        return result
                    return -1
            if l > 0 and nums[l] == nums[l-1]:
                return nums[l]
            if l < nums_len-1 and nums[l] == nums[l+1]:
                return nums[l]
            if r > 0 and nums[r] == nums[r-1]:
                return nums[l]
            if r < nums_len-1 and nums[r] == nums[r+1]:
                return nums[r]
            return -1
        return check(l, r, nums)




if __name__ == '__main__':

    # nums = [1, 3, 4, 2, 2]
    # # 输出：2

    # nums = [3, 1, 3, 4, 2]
    # # 输出：3


    nums = [3, 3, 3, 3, 3]
    # 输出：3

    # nums = [11, 5, 2, 3, 11]

    solution = Solution()
    result = solution.findDuplicate(nums)
    print(result)