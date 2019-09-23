class Solution:
    def addBinary(self, a: str, b: str) -> str:
        aNum, bNum = 0, 0
        for ch in a:
            aNum = aNum<<1 | int(ch)
        for ch in b:
            bNum = bNum<<1 | int(ch)
        sumNum = aNum+bNum
        sumStr = []
        while sumNum>0:
            sumStr.append(str(sumNum&1))
            sumNum = sumNum>>1
        sumStr = list(reversed(sumStr))
        if len(sumStr) == 0:
            return '0'
        return ''.join(sumStr)
if __name__ == '__main__':
    solution = Solution()
    print(solution.addBinary("11", "1"))