# https://medium.com/basecs/trying-to-understand-tries-3ec6bede0014
class TrieNode:
    def __init__(self):
        self.children = {}
        self.terminal = False
        self.data = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:

        cur = self.root
        for ch in word:
            if not cur.children.get(ch):
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.terminal = True

    def search(self, word: str) -> bool:
        cur = self.root
        for ch in word:
            if not cur.children.get(ch):
                return False
            cur = cur.children[ch]
        return cur.terminal

    def startsWith(self, prefix: str) -> bool:

        cur = self.root

        for ch in prefix:
            if not cur.children.get(ch):
                return False
            cur = cur.children[ch]
        return True
