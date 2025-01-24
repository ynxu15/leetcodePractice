'''
应用场景
比如给定了若干元素，要求统计出不同区间范围内，元素的个数。

这个代码是范围增加和查询 求和
'''
from typing import  List
class SegmentTreeAddQuerySum:
    def __init__(self):
        # self.num = []  # 初始数组
        # self.sum = []  # 总和树结构
        # self.add = []  # 懒数组 增加值
        pass

    def build(self, origin: List[int]):
        self.N = len(origin)+1
        N = self.N
        self.num = [0]*(N+1)
        for i in range(N):
            self.num[i+1] = origin[i]

        self.sum = [0] * (N << 2)
        self.add = [0] * (N << 2)
        self.buildHelp(1, N, 1)  # 是从下标0开始的，因此左子树是index << 1， 右子树是 index << 1|1; 边界 [l, r]


    def buildHelp(self, l, r, index):
        '''
        # L 要处理的范围，左边界
        # R 要处理的范围， 右边界
        l 当前节点代表的左边界
        r 当前节点代表的右边界
        index 当前节点下标
        '''
        if l == r:
            self.sum[index] = self.num[l]
            return

        mid = (l+r) >> 1
        self.buildHelp(l, mid, index << 1)  # 左子树
        self.buildHelp(mid+1, r, (index << 1) | 1) # 右子树
        self.up(index)  # 向上更新 根据子树位置，更新index位置sum

    def up(self, index):
        self.sum[index] = self.sum[index << 1] + self.sum[(index << 1)|1]

    def down(self, index, ln, rn):
        '''
        :param index:
        :param ln:  左侧有几个数
        :param rn:  右侧有几个数
        :return:
        '''
        print(index, len(self.num), len(self.add))
        if self.add[index] != 0:
            self.lazy(index << 1, self.add[index], ln)
            self.lazy(index << 1|1, self.add[index], rn)
            self.add[index] = 0

    def lazy(self, index, value, n):
        self.sum[index] += value*n
        self.add[index] += value

    def addOne(self, jobl, jobr, job_value,  l=None,  r=None, index=None):
        if not l:
            l, r, index = 1, self.N, 1

        if jobl < l and r <= jobr:
            self.lazy(index, job_value, r-l+1)
            return

        mid = (l+r) >> 1
        self.down(index, mid-l+1, r-mid)
        if jobl <= mid:
            self.addOne(jobl, jobr, job_value, l, mid, index<<1)  # 左子树
        if jobr>mid:
            self.addOne(jobl, jobr, job_value, mid+1, r, index<<1|1)  # 右子树
        self.up(index)  # 向上更新

    def query(self, jobl, jobr, l=None, r=None, index=None):
        if jobl <= l and jobr >= r:
            return self.sum[index]

        mid = (l+r) >> 1
        self.down(index, mid-l+1, r-mid)
        ans = 0
        if jobl <= mid:
            ans += self.query(jobl, jobr, l, mid, index<<1)  # 左子树
        if jobr > mid:
            ans += self.query(jobl, jobr, mid+1, r, index<<1|1)  # 右子树
        return ans

    def toString(self):
        results = []
        self.toStringHelper(1, len(self.num)-1, results, 1)
        return "".join(results)

    def toStringHelper(self, l, r, results, index):
        queue = []
        queue.append([index, l, r])
        while queue:
            size = len(queue)
            for i in range(size):
                now = queue.pop(0)
                results.append(f"[{now[1]}, {now[2]}] sum: {self.sum[now[0]]}")
                if self.add[now[0]] != 0:
                    results.append(f", lazy: {self.lazy[now[0]]}")
                # if self.update[now[0]]:
                #     results.append(f", change: {self.change[now[0]]}")
                results.append("}\t")
                if now[1] != now[2]:
                    mid = now[1] + (now[2]-now[1]) >>1
                    queue.append([now[0]<<1, now[1], mid])
                    queue.append([now[0]<<1|1, mid+1, now[2]])
        results.append("\n")


if __name__ == '__main__':
    iTree = SegmentTreeAddQuerySum()
    iTree.build([1, 1, 1, 1, 1, 1])
    print("================原始树===================")
    # print(iTree.toString())
    print(" [1, 5]范围内增加1后查询")
    iTree.addOne(1, 5, 1)
    #print(iTree.toString())
    print(iTree.query(3, 6))

    # iTree.update(1, 4, 4)
    # print(iTree.toString())
    # iTree.query(1, 6)
    # iTree.query(3, 6)