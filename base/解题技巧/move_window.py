'''
滑动窗口解题框架
'''

left, right = 0, 0
nums = []
window = []
while right < len(nums):
    window.append(nums[right])
    right += 1

    while window needs shrink:
        window.remove(nums[left])
        left += 1