
'''
用类描述实现前缀树，占用内存多，速度慢
'''

class TrieNode:
    def __init__(self):
        self.pass1, self.end = 0, 0
        self.nexts = {}
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        node.pass1 += 1
        for i in range(len(word)):
            path = word[i]
            if not path in node.nexts:
                node.nexts[path] = TrieNode()
            node = node.nexts[path]
            node.pass1 += 1
        node.end += 1

    def erase(self, word: str):
        '''删除一个字符串'''
        if self.countWordsEqualsTo(word) > 0:
            node = self.root
            node.pass1 -= 1
            for i in range(len(word)):
                path = word[i]
                node.nexts[path].pass1 -= 1
                if node.nexts[path].pass1 == 0:
                    del node.nexts[path]
                    return
                node = node.nexts[path]
            node.end -= 1

    def countWordsEqualsTo(self, word: str):
        node = self.root
        for i in range(len(word)):
            path = word[i]
            if not path in node.nexts:
                return 0
            node = node.nexts[path]
        return node.end

    def countWordsStartingWith(self, pre: str):
        node = self.root
        for i in range(len(pre)):
            path = pre[i]
            if not path in node.nexts:
                return 0
            node = node.nexts[path]
        return node.pass1

if __name__ == '__main__':
    trie = Trie()

    trie.insert("hello")
    trie.insert("world")
    trie.insert("helloworld")
    trie.insert("hello")
    trie.insert("hellohahha")

    print(trie.countWordsEqualsTo("hello"))
    print(trie.countWordsStartingWith("hello"))
    trie.erase("hello")
    trie.erase("hell")
    print(trie.countWordsEqualsTo("hello"))
