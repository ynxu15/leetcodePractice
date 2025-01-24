'''
堆排序
'''


def heapSort1(nums):
    # // 从顶到底建立大根堆，O(n * logn)
    # // 依次弹出堆内最大值并排好序，O(n * logn)
    # // 整体时间复杂度O(n * logn)
    n = len(nums)
    for i in range(n):
        heapInsert(nums, i)
    size = n
    while size > 1:
        size -= 1
        nums[0], nums[size] = nums[size], nums[0]
        heapify(nums, 0, size)

def heapSort2(nums):
    # // 从底到顶建立大根堆，O(n)
    # // 依次弹出堆内最大值并排好序，O(n * logn)
    # // 整体时间复杂度O(n * logn)
    n = len(nums)
    for i in range(n-1, -1, -1):
        heapify(nums, i, n)
    size = n
    while size > 1:
        size -= 1
        nums[0], nums[size] = nums[size], nums[0]
        heapify(nums, 0, size)

def heapInsert(nums, i):  # 是把尾巴上的元素升上去
    father_index = (i-1)//2
    while father_index >-1 and nums[i] > nums[father_index]:
        nums[i], nums[father_index] = nums[father_index], nums[i]
        i = father_index
        father_index = (i-1)//2

def heapify(nums, i, size):  # 是将头的元素降下去
    # // i位置的数，变小了，又想维持大根堆结构
    # // 向下调整大根堆
    # // 当前堆的大小为size
    l = i*2+1
    while l<size:
        # 有左孩子 l
        # 右孩子 l+1
        # 评选哪个孩子更强
        best = l + 1 if nums[l+1] > nums[l] else l
        best = best if nums[best] > nums[i] else i
        if best == i:
            break
        nums[best], nums[i] = nums[i], nums[best]
        i = best
        l = i * 2 + 1
