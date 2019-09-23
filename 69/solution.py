class Solution:
    def mySqrt(self, x: int) -> int:
        def sqrt(x, l, r):
            if l == r:
                return max(l - 1, 1)
            if r - l == 1:
                return l
            mid = (l + r) // 2
            mid2 = mid ** 2
            if mid2 == x:
                return mid
            if mid2 > x:
                return sqrt(x, l, mid)
            if mid2 < x:
                return sqrt(x, mid, r)
        if x == 1:
            return 1
        else:
            return sqrt(x, 1, x)

if __name__ == '__main__':
    solution = Solution()
    print(solution.mySqrt(8))