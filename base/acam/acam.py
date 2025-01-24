

class ACAM:
    def __init__(self, strings):
        # 目标字符串数量
        self.MAXN = 2000001
        # 目标字符串总的字符数量
        self.MAXS = 2000001

        # 每个字符串，结尾节点的编号
        self.end = [0] * (self.MAXN)

        self.tree = [[0]*26 for _ in range(self.MAXS)]
        self.fail = [0] * (self.MAXS)
        self.cnt = 0

        # 题目相关
        # 这里是统计词频
        self.times = [0] * self.MAXS
        # 堆栈或者队列，临时用的
        self.box = [0] * self.MAXS

        # 链式前向星，为了建立fail指针的反图
        self.head = [0] * self.MAXS
        self.next = [0] * self.MAXS
        self.to = [0] * self.MAXS
        self.edge = 0

        # 递归改成非递归，用到的
        self.visited = [False] * self.MAXS
        self.build(strings)

    def build(self, strings):
        self.N = len(strings)
        for i, s in enumerate(strings):
            self.insert(i, s)

    def insert(self, i, s: str):
        '''
        自动机加入目标字符串
        i: 字符串编号
        s: 字符串
        '''
        u = 0  # 0 是头结点  self.tree[u][c] 是u通过c指向的孩子节点下标
        for j in range(len(s)):
            c = ord(s[j]) - ord('a')
            if self.tree[u][c] == 0:
                self.cnt += 1
                self.tree[u][c] = self.cnt
            u = self.tree[u][c]
        # 每个字符串结尾节点编号。
        self.end[i] = u

    def set_fail(self):
        # // 加入所有目标字符串之后
        # // 设置fail指针 以及 设置直接直通表
        # // 做了AC自动机固定的优化

        # 层序遍历树，设置指针
        l, r = 0, 0  # [l, r) 区间
        for i in range(26):
            if self.tree[0][i] > 0:
                self.box[r] = self.tree[0][i]
                r += 1
        while l < r:
            u = self.box[l]
            l += 1
            for i in range(26):
                if self.tree[u][i] == 0:   # 没有子节点了。
                    self.tree[u][i] = self.tree[self.fail[u]][i]  # ？？ 这个没明白
                else:
                    self.fail[self.tree[u][i]] = self.tree[self.fail[u]][i]  # 设置子节点的fail指针为父亲节点的fail指针的子节点
                    self.box[r] = self.tree[u][i]
                    r += 1

    def addEdge(self, u, v):
        self.edge += 1
        self.next[self.edge] = self.head[u]
        self.head[u] = self.edge
        self.to[self.edge] = v

    def f1(self, u):
        i = self.head[u]  # u节点出发的所有边，里面的第一个边. i 是边的下标
        while i > 0:
            self.f1(self.to[i])  # 意思应该是，先把所有后续节点都搞完，然后统计到当前节点
            self.times[u] += self.times[self.to[i]]
            i = self.next[i]

    # 非递归模式
    def f2(self, u):
        r = 0
        self.box[r] = u
        r += 1
        while r > 0:
            cur = self.box[r-1]
            if not self.visited[cur]:
                self.visited[cur] = True
                i = self.head[cur]
                while i > 0:
                    self.box[r] = self.to[i]
                    r += 1
                    i = self.next[i]
            else:
                r -= 1
                i = self.head[cur]
                while i > 0:
                    self.times[cur] += self.times[self.to[i]]
                    i = self.next[i]

    def match(self, article):
        u = 0  # 节点编号
        for i, c in enumerate(article):
            u = self.tree[u][ord(c)-ord('a')]
            self.times[u] += 1
        #根据fail指针建反图
        for i in range(1, self.cnt+1):  # 遍历除root以外的所有节点
            self.addEdge(self.fail[i], i)  # i 匹配失败了，要跳转到 fail[i],现在创建了 fail[i] -> i 的边
        # // 遍历fail指针建的树
        # // 汇总每个节点的词频
        self.f2(0)
        for i in range(1, self.N+1):
            print(self.times[self.end[i]])