'''
应用场景
比如给定了若干元素，要求统计出不同区间范围内，元素的个数。
'''
from typing import  List
class IntervalTree:
    def __init__(self):
        self.num = []  # 初始数组
        self.sum = []  # 总和树结构
        self.lazy = []  # 懒数组
        self.update = []  # 懒更新
        self.change = []  # 懒更新的值

    def build(self, origin: List[int]):
        N = len(origin)
        self.num = [0]*(N+1)
        for i in range(N):
            self.num[i+1] = origin[i]

        sum = [0] * (N << 2)
        lazy = [0] * (N << 2)
        lazy = [False] * (N << 2)
        change = [0] * (N << 2)
        self.buildHelp(1, N, 1, N, 1)  # 是从下标0开始的，因此左子树是index << 1， 右子树是 index << 1|1; 边界 [l, r]


    def buildHelp(self, L, R, l, r, index):
        '''
        L 要处理的范围，左边界
        R 要处理的范围， 右边界
        l 当前节点代表的左边界
        r 当前节点代表的右边界
        index 当前节点下标
        '''
        if l == r:
            self.sum[index] = self.num[l]
            return

        mid = l+(r-l)//2
        if L <= mid:
            self.buildHelp(L, R, l, mid, index << 1)  # 左子树
        if R > mid:
            self.buildHelp(L, R, mid+1, r, (index << 1) | 1) # 右子树

        self.pushUp(index)  # 向上更新

    def pushUp(self, index):
        self.sum[index] = self.sum[index << 1] + self.sum[(index << 1)|1]

    def add(self, L, R, add_num):
        self.addHelp(L, R, 1, len(self.num)-1, 1, add_num)

    def addHelp(self, L, R, l, r, index, add_num):
        if L <= l and R >= r:
            self.lazy[index] += add_num
            self.sum[index] += (r-l+1) * add_num

        mid = l + (r - l) // 2
        self.pushDown(index, mid-l+1, r-mid)
        if L <= mid:
            self.addHelp(L, R, l, mid, index << 1, add_num)  # 左子树
        if R > mid:
            self.addHelp(L, R, mid + 1, r, (index << 1) | 1, add_num)  # 右子树

        self.pushUp(index)  # 向上更新

    def pushDown(self, index, ln, rn):
        if self.update[index]:
            self.update[index << 1] = True
            self.change[index << 1] = self.change[index]
            self.sum[index << 1] = self.change[index] * ln
            self.lazy[index << 1] = 0

            self.update[index << 1 | 1] = True
            self.change[index << 1 | 1] = self.change[index]
            self.sum[index << 1 | 1] = self.change[index] * rn
            self.lazy[index << 1 | 1] = 0
            self.update[index] = False

        if self.lazy[index] != 0:
            self.lazy[index << 1] += self.lazy[index]
            self.lazy[index << 1 | 1] += self.lazy[index]

            self.sum[index << 1] += self.lazy[index] * ln
            self.sum[index << 1 | 1] += self.lazy[index] * rn
            self.lazy[index] = 0

    def update(self, L, R, val):
        self.updateHelp(L, R, val, 1, len(self.num)-1, 1)

    def updateHelp(self, L, R, val, l, r, index):
        if L <= l and R >= r:
            self.update[index] = True
            self.change[index] = val
            self.sum[index] = val*(r-l+1)
            return

        mid = l + (r - l) // 2
        self.pushDown(index, mid-l+1, r-mid)
        if L <= mid:
            self.updateHelp(L, R, val, l, mid, index << 1)  # 左子树
        if R > mid:
            self.updateHelp(L, R, val, mid + 1, r, (index << 1) | 1)  # 右子树

        self.pushUp(index)  # 向上更新

    def query(self, L, R):
        result = self.queryHelp(L, R, 1, len(self.nums)-1, 1)
        return f"query[{L},{R}]: {result}"

    def queryHelp(self, L, R, l, r, index):
        if L <= l and R >= r:
            return self.sum[index]

        mid = l + (r - l) // 2
        self.pushDown(index, mid-l+1, r-mid)
        ret = 0
        if L <= mid:
            ret += self.queryHelp(L, R, l, mid, index << 1)  # 左子树
        if R > mid:
            ret += self.queryHelp(L, R, mid + 1, r, (index << 1) | 1)  # 右子树

        #self.pushUp(index)  # 向上更新

    def toString(self):
        results = []
        self.toStringHelper(1, len(self.nums)-1, results, 1)
        return "".join(results)

    def toStringHelper(self, l, r, results, index):
        queue = []
        queue.add([index, l, r])
        while queue:
            size = len(queue)
            for i in range(size):
                now = queue.pop(0)
                results.append(f"[{now[1]}, {now[2]}] sum: {self.sum[now[0]]}")
                if self.lazy[now[0]] != 0:
                    results.append(f", lazy: {self.lazy[now[0]]}")
                if self.update[now[0]]:
                    results.append(f", change: {self.change[now[0]]}")
                results.append("}\t")
                if now[1] != now[2]:
                    mid = now[1] + (now[2]-now[1]) >>1
                    queue.append([now[0]<<1, now[1], mid])
                    queue.append([now[0]<<1|1, mid+1, now[2]])
        results.append("\n")


if __name__ == '__main__':
    iTree = IntervalTree([1, 1, 1, 1, 1, 1])
    print("================原始树===================")
    print(iTree.toString())
    print(" [1, 5]范围内增加1后查询")
    iTree.add(1, 5, 1)
    print(iTree.toString())
    print(iTree.query(3, 6))

    iTree.update(1, 4, 4)
    print(iTree.toString())
    iTree.query(1, 6)
    iTree.query(3, 6)