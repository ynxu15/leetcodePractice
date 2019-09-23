class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=3:
            return n
        numSmall, numBig = 1, 2
        for i in range(n-2):
            numSmall, numBig = numBig, numSmall+numBig
        return numBig

if __name__ == '__main__':
    print(Solution().climbStairs(4))