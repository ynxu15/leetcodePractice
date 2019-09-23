class Solution:
    def searchInsert(self, nums, target: int) -> int:
        def search(nums, target, l, r):
            if l == r:
                return l
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                return search(nums, target, l, mid)
            if nums[mid] < target:
                return search(nums, target, min(mid + 1, r), r)

        return search(nums, target, 0, len(nums))

if __name__ == '__main__':
    solution = Solution()
    print(solution.searchInsert([1,3], 2))