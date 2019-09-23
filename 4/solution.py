class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1, r1, l2, r2 = 0, len(nums1), 0, len(nums2)
        avgNum = (r1 + r2)/2.0
        lefNum, rightNum = 0, 0
        def findNum(nums, l2, r2):
            pass
        def findMedian():
            if r1-l1 > r2-l2:
                mid1 = (l1 + r1)//2
                mid2 = findNum(nums2, l2, r2, nums1[mid1])
            else:
                mid2 = (l2 + r2)//2
                mid1 = findNum(nums1, l1, r1, nums2[mid2])
            if leftNum + (mid1-l1) + (mid2-l2)>=avgNum:
                leftNum += ((mid1 - l1) + (mid2 - l2))
                return findMedian()
            else:
                rightNum += ((r1-mid1) + (r2-mid2))
                return findMedian()


if __name__ == "__main__":
    print(Solution().findMedianSortedArrays([1,3], [2]))