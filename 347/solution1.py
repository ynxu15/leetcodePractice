from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return
        nums_map = {}
        for n in nums:
            if n in nums_map:
                nums_map[n] += 1
            else:
                nums_map[n] = 1

        # 堆排序
        heap = []
        heap_count = 0
        for n in nums_map:
            count = nums_map[n]
            if heap_count < k:
                heap.append((n, count))
                heap_count += 1
                # 修正小顶堆
                i = heap_count-1
                while i > 0:
                    i_parent = (i-1) >> 1
                    if heap[i_parent][1] > heap[i][1]:
                        heap[i_parent], heap[i] = heap[i], heap[i_parent]
                    i = i_parent
            else:
                if heap[0][1] < count:
                    heap[0] = (n, count)
                    # 修正小顶堆
                    i = 0
                    while i < heap_count:
                        l = 2*i+1
                        r = l+1
                        if l < heap_count:
                            if r < heap_count:
                                min_index = l if heap[l][1] < heap[r][1] else r
                            else:
                                min_index = l
                            #交换
                            if heap[i][1] > heap[min_index][1]:
                                heap[i], heap[min_index] = heap[min_index], heap[i]
                            i = min_index
                        else:
                            # 父亲节点超出了界限
                            break
        return [r[0] for r in heap]


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    # 输出: [1, 2]

    # nums = [1]
    # k = 1
    # # 输出: [1]

    solution = Solution()
    result = solution.topKFrequent(nums, k)
    print(result)