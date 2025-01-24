



class Bitset:
    def __init__(self, n):
        '''
        要能放入0-n-1这n个数
        :param n:
        '''
        # a / b如果结果想向上取整，可以写成: (a + b - 1) / b
        # 前提是a和b都是非负数
        self.bitset = [0]*((n+31)//32) # 每个数可以表示32位，即32个数

    def add(self, num):
        self.bitset[num//32] |= 1 << (num%32)  # num//32是找到具体哪个数表示这个bit, 1<<(num%32)是这个数的第几位表示这个数

    def remove(self, num):
        self.bitset[num//32] &= ~(1<<(num%32))

    def reverse(self, num):
        self.bitset[num//32] ^= 1<<(num%32)

    def contains(self, num):
        return ((self.bitset[num//32] >> (num%32)) &1 )== 1

if __name__ == '__main__':
    import random
    n = 1000
    testTimes = 10000
    print("测试开始")
    # 实现的位图结构
    bitset = Bitset(n)
    # 直接用HashSet做对比测试
    pySet = set()
    print("调用阶段开始")
    for i in range(testTimes):
        decide = random.random()
        number = (int) (random.random() * n)
        if decide < 0.333:
            bitset.add(number)
            pySet.add(number)
        elif decide < 0.666:
            bitset.remove(number)
            if number in pySet:
                pySet.remove(number)
        else:
            bitset.reverse(number)
            if number in pySet:
                pySet.remove(number)
            else:
                pySet.add(number)

    print("调用阶段结束")
    print("验证阶段开始")
    for i in range(n):
        if bitset.contains(i) != (i in pySet):
            print("出错了： ", i)
    print("验证阶段结束")
    print("测试结束")