'''
!!! 树状数组下标要从1开始

举例，一个数的下标是 i，它表示的是从index_low- i之间的数的和
index_low的计算方式是 i 去掉最右侧的一个1，然后再加1
例如： i = 1  -> 0001 -> 0001 -> index_low = 1
例如： i = 2 -> 0010 -> 0001 -> index_low = 1
例如： i = 3  -> 0011 -> 0011 -> index_low = 3
'''

class IndexTree:
    def __init__(self, maxN = 100000):
        self.MAXN = maxN
        self.tree = [0]*self.MAXN
        self.m = 0
        self.n = 0

    def lowbit(self, i):
        return i & (-i)

    def add(self, i, v):
        while i<=self.MAXN:
            self.tree[i] += v
            i += self.lowbit(i)

    def range_add(self, l, r, v):
        '''
        原始数组中，l-r中间的每个数值+v
        :param l:
        :param r:
        :param v:
        :return:
        '''
        self.add(l, v)
        self.add(r+1, -v)

    def sum(self, i):
        '''
        计算 1-i之间数的和
        :param i:
        :return:
        '''
        ans = 0
        while i > 0:
            ans += self.tree[i]
            i -= self.lowbit(i)
        return ans

    def range(self, l, r):
        '''
        计算l - r区间的数据的和
        :param l:
        :param r:
        :return:
        '''
        return self.sum(r)-self.sum(l)


if __name__ == '__main__':
    indexTree = IndexTree()
    n = input()
    m = input()
    for i in range(n):
        value = input()
        indexTree.add(i, value)

    for i in range(m):
        a, b, c = input(), input(), input()
        if a == 1:
            indexTree.add(b, c)
        else:
            print(indexTree.range(b, c))
