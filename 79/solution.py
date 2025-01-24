from typing import List

'''
todo 双向链表+字典实现。能够实现O（1）时间复杂度的节点移动
'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        index_map = {}
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c not in index_map:
                    index_map[c] = []
                index_map[c].append((i, j))
        if not word:
            return False

        m, n = len(board), len(board[0])


        c0 = word[0]
        visited = set()
        match_count = 0
        word_len = len(word)
        if c0 not in index_map:
            return False
        def matchHelp(match_count, i, j):
            if match_count == word_len:
                return True

            i_tmp, j_tmp = i-1, j
            if i > 0 and not (i_tmp, j_tmp) in visited and word[match_count] == board[i_tmp][j_tmp]: # 左侧搜索
                visited.add((i_tmp, j_tmp))
                r = matchHelp(match_count +1, i_tmp, j_tmp)
                if r:
                    return True
                visited.remove((i_tmp, j_tmp))

            i_tmp, j_tmp = i+1, j
            if i < m-1 and not (i_tmp, j_tmp) in visited and word[match_count] == board[i_tmp][j_tmp]: # 右侧搜索
                visited.add((i_tmp, j_tmp))
                r = matchHelp(match_count +1, i_tmp, j_tmp)
                if r:
                    return True
                visited.remove((i_tmp, j_tmp))

            i_tmp, j_tmp = i, j-1
            if j > 0 and not (i_tmp, j_tmp) in visited and word[match_count] == board[i_tmp][j_tmp]: # 上方搜索
                visited.add((i_tmp, j_tmp))
                r = matchHelp(match_count +1, i_tmp, j_tmp)
                if r:
                    return True
                visited.remove((i_tmp, j_tmp))

            i_tmp, j_tmp = i, j + 1
            if j < n-1 and not (i_tmp, j_tmp) in visited and word[match_count] == board[i_tmp][j_tmp]: # 下方搜索
                visited.add((i_tmp, j_tmp))
                r = matchHelp(match_count + 1, i_tmp, j_tmp)
                if r:
                    return True
                visited.remove((i_tmp, j_tmp))
            return False

        for index in index_map[c0]:
            visited.add(index)
            r = matchHelp(1, index[0], index[1])
            if r:
                return True
            visited.remove(index)
        return False

if __name__ == '__main__':
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    # 输出 true

    # board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    # word = "SEE"
    # #输出：true

    # board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    # word = "ABCB"
    # #输出：false

    board =   [
        ["C", "A", "A"],
        ["A", "A", "A"],
        ["B", "C", "D"]
    ]

    word = "AAB"

    solution = Solution()
    result = solution.exist(board, word)
    print(result)

