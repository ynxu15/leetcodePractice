
'''
经验总结：
如果 左闭右闭 -> while 要使用小于等于 -> 无论哪个条件，都要mid+1或者mid-1，不能使用left = mid，或者right=mid。
如果 左闭右开 -> while 要使用小于 -> 后续可能出现 mid的情况
'''

#0, 1,2,2,3
#       ^ ^
def binary_search(nums, target):
    '''查找某个值'''
    left, right = 0, len(nums)-1

    while left <= right:
        mid = left + (right-left)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid+1
        elif nums[mid] > target:
            right = mid-1
    return -1


def binary_search_left_bound(nums, target):
    '''
    查找target的左侧边界
    [1,2,2,2,3] target 2
    返回 1
    '''
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        mid_num = nums[mid]
        if nums[mid] == target:
            right = mid - 1    # 要求左边界，这个等于条件这里，就要修改右侧指针；反之亦然
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
    return left

def binary_search_right_bound(nums, target):  # 确认数一定在
    '''
    查找target的右侧边界
    [1,2,2,2,3] target 2
    返回 3
    '''
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
    return right

if __name__ == '__main__':
    nums = [1, 2, 2, 2, 4]
    target = 2
    target = 3
    print(binary_search_right_bound(nums, target))
    #print(binary_search_left_bound(nums, target))