
def merge(nums, l, mid, r):
    help = [0] * len(nums)
    i, a, b = l, l, mid+1
    while a<=mid and b<=r:
        if nums[a] <= nums[b]:
            help[i] = nums[a]
            a += 1
        else:
            help[j] = nums[b]
            b += 1
        i += 1

    while a<=mid:
        help[i] = nums[a]
        i += 1
        a += 1
    while b<=r:
        help[i] = nums[b]
        i += 1
        b += 1
    for i in range(l, r+1):
        nums[i] = help[i]


def mergeSort1(nums, l, r):
    '''递归版'''
    if l == r:
        return

    mid = (l+r) // 2
    mergeSort1(nums, l, mid)
    mergeSort1(nums, mid+1, r)
    merge(nums, l, mid, r)

def mergeSort2(nums, l, r):
    '''非递归版'''
    nums_len = len(nums)
    l, m, r, step = 1, 1, 1, 1
    while step < nums_len:
        l = 0
        while l < nums_len:
            mid = l + step -1
            if mid+1 >=nums_len:
                break
            r = min(l + (step << 1)-1, nums_len-1)
            merge(l, mid, r)
            l = r+1