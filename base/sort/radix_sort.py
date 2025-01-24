'''
基数排序
'''

class RadixSort:

    def __init__(self):
        self.BASE = 10
        self.MAXN = 100001
        # self.arr = [0] * self.MAXN
        # self.help = [0] * self.MAXN
        self.cnts = [0] * self.BASE

        self.n = 0

    def sort(self, nums):
        '''映射成非负数，并找到最大值'''
        min_num = min(nums)
        max_num = -1
        for i in range(len(nums)):
            nums[i] -= min_num
        max_num = max(nums)
        self.radixSort(nums, self.bits(max))
        for i in range(len(nums)):
            nums[i] += min_num

    def bits(self, num):
        '''最大数有多少位'''
        ans = 0
        while num > 0:
            ans += 1
            num = num // self.BASE
        return ans

    def radixSort(self, nums, bits):

        n = len(nums)
        offset = 1
        while bits > 0:
            cnts = [0] * self.BASE
            hs = [0] * n
            for i in range(0, n):
                cnts[(nums[i] // offset)%self.BASE] += 1  # 取最低位的数

            for i in range(1, self.BASE):
                cnts[i] = cnts[i] + cnts[i-1]

            for i in range(n-1, -1, -1):  # 稳定的排序
                cnts[(nums[i]//offset)//self.BASE] -= 1
                hs[cnts[(nums[i]//offset)//self.BASE]] = nums[i]
            for i in range(n): # 刷回原数组
                nums[i] = hs[i]

            offset *= self.BASE  # 下一个更高位
            bits -= 1

