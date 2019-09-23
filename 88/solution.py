class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1Len, nums2Len = m, n
        if nums2Len == 0:
            return
        i,j = 0, 0
        while i<nums1Len and j <nums2Len:
            if nums1[i]<=nums2[j]:
                i += 1
            else:
                nums1.insert(i, nums2[j])
                i, j, nums1Len = i+1, j+1, nums1Len+1
                print(nums1)
        #print('ij',i,j)
        while j< nums2Len:
            nums1.insert(i, nums2[j])
            i, j, nums1Len = i+1, j+1, nums1Len+1
        #print(nums1)
        for _ in range(nums2Len):
            nums1.pop()
        #print(nums1)

if __name__ == "__main__":
    print(Solution().merge([1,2,3,0,0,0],3, [2, 5, 6],3))