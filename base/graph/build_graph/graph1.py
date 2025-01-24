

class Graph:
    def __init__(self, MAXN=11, MAXM=21):
        self.MAXN = MAXN # 节点最大数量
        # // 边的最大数量
        # // 只有链式前向星方式建图需要这个数量
        # // 注意如果无向图的最大数量是m条边，数量要准备m * 2
        # // 因为一条无向边要加两条有向边
        self.MAXM = MAXM # 边最大数量

        # 邻接矩阵方式
        self.graph1 = [ [0] * self.MAXN for _ in range(self.MAXN)]

        self.build()

    def build(self):
        # for i in range(self.MAXN):
        #     for j in range(self.MAXN):
        #         self.graph1[i][j] = 0
        pass

    def directGraph(self, edges):
        for edge in edges:
            # edge: [start, end, weight]
            self.graph1[edge[0]][edge[1]] = edge[2]

    def undirectGraph(self, edges):
        for edge in edges:
            # edge: [start, end, weight]
            self.graph1[edge[0]][edge[1]] = edge[2]
            self.graph1[edge[1]][edge[0]] = edge[2]

    def traversal(self, n):
        print("遍历邻接矩阵")
        for i in range(self.MAXN):
            for j in range(self.MAXN):
                print("%3d"%self.graph1[i][j], end=", ")
            print()
        print()


if __name__ == '__main__':
    #edges = [[] {] 1, 3, 6 }, { 4, 3, 4 }, { 2, 4, 2 }, { 1, 2, 7 }, { 2, 3, 5 }, { 3, 1, 1 } };
    pass