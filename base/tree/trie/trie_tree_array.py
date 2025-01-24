
'''
数组形式实现
'''
class TrieTree:
    def __init__(self, MAXN=1000001):
        self.MAXN = MAXN
        self.tree = [[0]*26 for _ in range(self.MAXN)]
        self.end = [0] * self.MAXN
        self.pass1 = [0] * self.MAXN
        self.cnt = 1  # 表示系统里现在有多少个节点了。root节点不存放数据，所以开始就有1个节点  tree[1] 是root节点

    def insert(self, word: str):
        cur = 1
        self.pass1[cur] += 1
        for i in range(0, len(word)):
            path = ord(word[i]) - ord('a')
            if self.tree[cur][path] == 0:
                self.cnt += 1
                self.tree[cur][path] = self.cnt  # 下一个节点的index
            cur = self.tree[cur][path]
            self.pass1[cur] += 1
        self.end[cur] += 1

    def search(self, word: str):
        cur = 1
        for i in range(len(word)):
            path = ord(word[i]) - ord('a')
            if self.tree[cur][path] == 0:
                return 0
            cur = self.tree[cur][path]
        return self.end[cur]

    def prefixNumber(self, pre: str):
        cur = 1
        for i in range(len(pre)):
            path = ord(pre[i])-ord('a')
            if self.tree[cur][path] == 0:
                return 0
            cur = self.tree[cur][path]
        return self.pass1[cur]

    def delete(self, word: str):
        if self.search(word) > 0:
            cur = 1
            self.pass1[cur] -= 1
            for i in range(len(word)):
                path = ord(word[i]) - ord('a')
                self.pass1[self.tree[cur][path]] -= 1
                if self.pass1[self.tree[cur][path]] == 0:
                    self.tree[cur][path] = 0
                    return

                cur = self.tree[cur][path]
            self.end[cur] -= 1

    def clear(self):
        for i in range(self.cnt):
            self.tree[i] = [0]*26
            self.end[i] = 0
            self.pass1[i] = 0


if __name__ == '__main__':
    trie = TrieTree()

    trie.insert("hello")
    trie.insert("world")
    trie.insert("helloworld")
    trie.insert("hello")
    trie.insert("hellohahha")

    print(trie.search("hello"))
    print(trie.prefixNumber("hello"))
    trie.delete("hello")
    trie.delete("hell")
    print(trie.search("hello"))
