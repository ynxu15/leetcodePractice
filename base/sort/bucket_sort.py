def Bucket_Sort(array, bucketsize):
    minValue = min(array)
    maxValue = max(array)
    res = []
    bucketcount = (maxValue - minValue) // bucketsize + 1
    bucket_lists = [[] for i in range(bucketcount)]

    for i in array:
        bucket_index = (i - minValue) // bucketsize
        bucket_lists[bucket_index].append(i)
    # 桶内排序
    for j in bucket_lists:
        #Quick_Sort_2(j, 0, len(j) - 1)
        j.sort()

    for j in bucket_lists:
        if len(j) != 0:
            res.extend(j)
    return res

from typing import List
def bucket_sort(arr:List[int]):
    """桶排序"""
    min_num = min(arr)
    max_num = max(arr)
    # 桶的大小
    bucket_range = (max_num-min_num) // len(arr)
    # 桶数组
    count_list = [[] for i in range(len(arr) + 1)]
    # 向桶数组填数
    for i in arr:
        count_list[int((i-min_num)//bucket_range)].append(i)
    arr.clear()
    # 回填，这里桶内部排序直接调用了sorted
    for i in count_list:
        for j in sorted(i):
            arr.append(j)