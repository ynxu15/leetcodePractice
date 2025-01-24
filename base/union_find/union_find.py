

class UnionFind:
    def __init__(self, n):
        self.MAXN = 1000001
        self.father = [-1] * self.MAXN
        self.size = [0] * self.MAXN
        self.stack = [0] * self.MAXN
        self.n = n
        self.build()

    def build(self):
        for i in range(self.n+1):
            self.father[i] = i
            self.size[i] = 1

    def find(self, i):
        '''找到i所在集合的父亲节点'''
        size = 0
        while i != self.father[i]:
            self.stack[size] = i
            size += 1
            i = self.father[i]
        while size > 0:
            self.father[self.stack[size]] = i
            size -= 1
        return i

    def isSameSet(self, x, y):
        '''判断两个节点是否属于同一个集合'''
        return self.find(x) == self.find(y)

    def union(self, x, y):
        '''x和y所在集合进行合并'''
        fx = self.find(x)
        fy = self.find(y)
        if fx != fy:
            # 小的挂到大的上面
            if self.size[fx] >= self.size[fy]:
                self.size[fx] += self.size[fy]
                self.father[fy] = fx
            else:
                self.size[fy] += self.size[fx]
                self.father[fx] = fy

    def print(self):
        for i in range(self.n):
            print("%2d" % i, end=' ')
        print()
        for i in range(self.n):
            fi = self.find(i)
            print("%2d"%fi, end=' ')
        print()

if __name__ == '__main__':
    nums = [0, 1, 2, 3, 4, 5, 6]
    n = 7
    unions = [[1, 2], [1, 3], [5, 6]]

    uf = UnionFind(n)
    for u in unions:
        uf.union(u[0], u[1])
    uf.print()


