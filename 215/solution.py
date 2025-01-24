from typing import List

'''
O(N)
堆排序
'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return None

        if k > len(nums):
            return None

        heap = [] # 小顶堆， 维持元素个数为k个
        n_num = 0
        for n in nums:
            if n_num < k:
                heap.append(n)
                n_num += 1
                i = n_num-1
                while i > 0:
                    i_parent = int((i-1)/2)
                    if heap[i_parent] > heap[i]:
                        heap[i_parent], heap[i] = heap[i], heap[i_parent]
                    i = i_parent
            else:
                if heap[0] < n:
                    heap[0] = n
                # 下沉
                i=0
                while i < n_num:
                    left_index = 2*i+1
                    right_index = 2*i+2
                    if left_index < n_num:
                        if right_index < n_num:
                            min_index = left_index if heap[left_index] < heap[right_index] else right_index
                        else:
                            min_index = left_index
                        if heap[i] > heap[min_index]:
                            heap[i], heap[min_index] = heap[min_index], heap[i]
                            i = min_index
                        else:
                            break
                    else:
                        if right_index < n_num:
                            min_index = right_index
                            if heap[i] > heap[min_index]:
                                heap[i], heap[min_index] = heap[min_index], heap[i]
                                i = min_index
                            else:
                                break
                        else:
                            break

        return heap[0]


if __name__ == '__main__':
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    #输出: 5

    # nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    # k = 4
    # # 输出: 4

    solution = Solution()
    result = solution.findKthLargest(nums, k)
    print(result)