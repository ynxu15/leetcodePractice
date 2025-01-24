'''
选择排序
时间复杂度 N^2
空间复杂度 1
不是稳定排序
是原地排序
'''
from typing import List
def sort(nums: List[int]) -> None:
    n = len(nums)
    # sortedIndex 是一个分割线
    # 索引 < sortedIndex 的元素都是已排序的
    # 索引 >= sortedIndex 的元素都是未排序的
    # 初始化为 0，表示整个数组都是未排序的
    sortedIndex = 0
    while sortedIndex < n:
        # 找到未排序部分 [sortedIndex, n) 中的最小值
        minIndex = sortedIndex
        for i in range(sortedIndex + 1, n):
            if nums[i] < nums[minIndex]:
                minIndex = i
        # 交换最小值和 sortedIndex 处的元素
        nums[sortedIndex], nums[minIndex] = nums[minIndex], nums[sortedIndex]

        # sortedIndex 后移一位
        sortedIndex += 1


def selectionSort(nums):
    if not nums:
        return
    nums_len = len(nums)
    for i in range(nums_len):
        minIndex = i
        for j in range(i+1, nums_len):
            if nums[j] < nums[minIndex]:
                minIndex = j
        if minIndex != i:
            nums[i], nums[minIndex] = nums[i], nums[minIndex]

def bubbleSort(nums):
    if not nums:
        return
    nums_len = len(nums)
    for end in range(nums_len-1, -1, -1):
        for i in range(end):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]


def insertSort(nums):
    if not nums:
        return
    nums_len = len(nums)
    for i in range(1, nums_len):
        for j in range(i-1, -1, -1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
            else:
                break

