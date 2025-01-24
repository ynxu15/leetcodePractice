from typing import List

'''
后续可以修改为递归的方式做
'''

class Solution:

    def numSquares2(self, n: int) -> int:
        # 先找平方数，然后转化为找零钱问题。 超内存
        # 1, 2, 3, 4
        # 1 4 9 16
        # 计算出所有的平方数
        import math
        K = int(math.sqrt(n))+1
        squares = [i**2 for i in range(1, K)]
        result_map = {}
        def findNumSquares(n: int, k):
            square = squares[k]
            if (n, k) in result_map:
                return result_map[(n, k)]
            if k < 0 or n < 0:
                return 100000000
            if n == 0:  # 找到了
                return 0
            elif n < squares[k]:  # 平方数太大了
                result = findNumSquares(n, k-1)
                if result < 100000000:
                    result_map[(n,k)] = result
                return result
            else:
                result1 = findNumSquares(n-squares[k], k)
                result2 = findNumSquares(n, k-1)
                result = min(result1+1, result2)
                if result < 100000000:
                    result_map[(n, k)] = result
                return result
        result = findNumSquares(n, K-2)
        return result

    def numSquares1(self, n: int) -> int:
        # 超时
        # 先找平方数，然后转化为找零钱问题。
        # 1, 2, 3, 4
        # 1 4 9 16
        # 计算出所有的平方数
        import math
        K = int(math.sqrt(n))+1
        squares = [i**2 for i in range(1, K)]
        def findNumSquares(n: int, k):
            if k < 0 or n < 0:
                return 100000000
            if n == 0:  # 找到了
                return 0
            elif n < squares[k]:  # 平方数太大了
                result = findNumSquares(n, k-1)
                return result
            else:
                result1 = findNumSquares(n-squares[k], k)
                result2 = findNumSquares(n, k-1)
                return min(result1+1, result2)
        result = findNumSquares(n, K-2)
        return result


    def numSquares(self, n: int) -> int:
        '''动态规划的思路做'''
        import math
        K = int(math.sqrt(n))+1
        squares = [i**2 for i in range(0, K)]  # 从0开始
        result = [0, 1]
        for i in range(2, n+1):
            minCount = 10000000
            for j in range(1, K):
                if i - squares[j] >= 0:
                    r = result[i-squares[j]]
                    if minCount > r:
                        minCount = r
                else:
                    break
            result.append(minCount+1)
        # print(list(range(n+1)))
        return result[n]

if __name__ == '__main__':
    # n = 12
    # # 输出：3

    # n = 13
    # #输出：2

    n = 22
    #3

    solution = Solution()
    result = solution.numSquares(n)
    print(result)