from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''DAG'''
        # 计算各个节点的入度
        degree_map = {i:0 for i in range(numCourses)}
        after_p_map = {i:[] for i in range(numCourses)}
        for p in prerequisites:
            degree_map[p[0]] += 1
            after_p_map[p[1]].append(p[0])
        d = sorted(list(degree_map.items()), key=lambda x:x[1])
        while d and d[0][1] == 0:
            c = d.pop(0)[0]
            del degree_map[c]
            # 减少依赖
            for c1 in after_p_map[c]:
                degree_map[c1] -= 1
            d = sorted(list(degree_map.items()), key=lambda x: x[1])
        if d:
            return False
        return True

    def canFinish2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''使用图遍历的方式解决，比我的快，我估计是因为频繁创建和删除元素导致的。遍历都比创建和删除速度快'''
        import collections
        edges = collections.defaultdict(list)
        visited = [0] * numCourses
        result = list()
        valid = True

        for info in prerequisites:
            edges[info[1]].append(info[0])

        def dfs(u: int):
            nonlocal valid
            visited[u] = 1
            for v in edges[u]:
                if visited[v] == 0:
                    dfs(v)
                    if not valid:
                        return
                elif visited[v] == 1:
                    valid = False
                    return
            visited[u] = 2
            result.append(u)

        for i in range(numCourses):
            if valid and not visited[i]:
                dfs(i)

        return valid

if __name__ == '__main__':
    numCourses = 2
    prerequisites = [[1, 0]]
    # 输出：true

    # numCourses = 2
    # prerequisites = [[1, 0], [0, 1]]
    # # 输出：false


    solution = Solution()
    result = solution.canFinish(numCourses, prerequisites)
    print(result)