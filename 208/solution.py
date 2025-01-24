from typing import List


class Node:
    def __init__(self):
        self.next = {}
        self.end = False

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.next:
                node.next[c] = Node()
            node = node.next[c]
        node.end = True
    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c in node.next:
                node = node.next[c]
            else:
                return False
        if len(node.next) == 0 or node.end:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c in node.next:
                node = node.next[c]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


if __name__ == '__main__':

    words = ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
    target = [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]

    obj = Trie()
    obj.insert(word)
    param_2 = obj.search(word)
    param_3 = obj.startsWith(prefix)
