'''
未测试
'''
class TopoSort:
    def __init__(self):
        self.MAXN = 1000
        self.MAXM = 1000
        self.graph = [[0]*self.MAXN for _ in range(self.MAXN)]
        self.indegree = [0] * self.MAXN

    def build(self, edges):
        '''必须是有向图'''
        for edge in edges:
            self.graph[edge[0]][edge[1]] = edge[2]
            self.indegree[edge[1]] += 1

    def sort(self):
        queue = [0] * self.MAXN
        l, r = 0, 0
        for i in range(self.MAXN):
            if self.indegree[i] == 0:
                queue[r] = i
                r += 1
        cnt = 0
        while l < r:
            cur = queue[l]
            l += 1
            cnt += 1
            for i in range(self.MAXN):
                if self.graph[cur][i] > 0:
                    self.indegree[i] -= 1
                    if self.indegree[i] == 0:
                        queue[r] = i
                        r += 1
        if cnt == self.MAXN:
            return queue
        else:
            return [0]

