class Solution:
    def plusOne(self, digits):
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            numTmp = digits[i] + carry
            carry, digits[i] = numTmp//10, numTmp%10
            if carry==0:
                break
        if carry == 1:
            digits.insert(0, carry)
        return digits

if __name__ == '__main__':
    solution = Solution()
    print(solution.plusOne([9]))