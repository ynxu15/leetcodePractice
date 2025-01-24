from typing import List

def sort(nums: List[int], num_count=3) -> None:  #  总共有num_count种类的数
    # 统计 0, 1, 2 出现的次数
    count = [0] * num_count
    for element in nums:
        count[element] += 1

    # 按照 count 数组的统计结果，依次填充原数组
    index = 0
    for element in range(num_count):
        for _ in range(count[element]):
            nums[index] = element
            index += 1