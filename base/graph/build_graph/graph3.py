
'''
链式前向星表示方法
'''
class Graph:
    def __init__(self, MAXN=11, MAXM=21):
        self.MAXN = MAXN # 节点最大数量
        # // 边的最大数量
        # // 只有链式前向星方式建图需要这个数量
        # // 注意如果无向图的最大数量是m条边，数量要准备m * 2
        # // 因为一条无向边要加两条有向边
        self.MAXM = MAXM # 边最大数量

        # 邻接矩阵方式
        #self.graph1 = [ [0] * self.MAXN for _ in range(self.MAXN)]
        #self.graph2 = []
        self.head = [0] * self.MAXN
        self.next = [0] * self.MAXM
        self.to = [0] * self.MAXM
        self.weight = [0] * self.MAXM # 边的权重
        self.cnt = 1

        self.build()

    def build(self):
        # for i in range(self.MAXN):
        #     for j in range(self.MAXN):
        #         self.graph1[i][j] = 0
        # for i in range(self.MAXN):
        #     self.graph2.append([])
        self.cnt = 1
        for i in range(len(self.head)):
            self.head[i] = 0

    def addEdge(self, u, v, w):
        '''u-> v, 权重w'''
        self.next[self.cnt] = self.head[u]
        self.to[self.cnt] = v
        self.weight[self.cnt] = w
        self.head[u] = self.cnt
        self.cnt += 1
    def directGraph(self, edges):
        for edge in edges:
            # edge: [start, end, weight]
            #self.graph1[edge[0]][edge[1]] = edge[2]
            #self.graph2[edge[0]].append([edge[1], edge[2]])
            self.addEdge(edge[0], edge[1], edge[2])

    def undirectGraph(self, edges):
        for edge in edges:
            # edge: [start, end, weight]
            # self.graph1[edge[0]][edge[1]] = edge[2]
            # self.graph1[edge[1]][edge[0]] = edge[2]

            # self.graph2[edge[0]].append([edge[1], edge[2]])
            # self.graph2[edge[1]].append([edge[0], edge[2]])

            self.addEdge(edge[0], edge[1], edge[2])
            self.addEdge(edge[1], edge[0], edge[2])

    def traversal(self, n):
        # print("遍历邻接矩阵")
        # for i in range(self.MAXN):
        #     for j in range(self.MAXN):
        #         print("%3d"%self.graph1[i][j], end=", ")
        #     print()
        # print()

        # print("遍历邻接表")
        # for i in range(self.MAXN):
        #     print("节点 %3d 的 （邻居，权重）"%i)
        #     for edge in self.graph2[i]:
        #         print("(%3d, %3d)"%(edge[0], edge[1]), end=", ")
        #     print()
        # print()

        print("遍历前向星")
        for i in range(1, self.MAXN):
            print("节点 %3d 的 （邻居，权重）"%i)
            edge_index = self.head[i]
            while edge_index > 0:
                print("(%3d, %3d)" % (self.to[edge_index], self.weight[edge_index]), end=", ")
                edge_index = self.next[edge_index]
            print()
        print()

if __name__ == '__main__':
    #edges = [[] {] 1, 3, 6 }, { 4, 3, 4 }, { 2, 4, 2 }, { 1, 2, 7 }, { 2, 3, 5 }, { 3, 1, 1 } };
    pass