class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            if cur.children.get(char, None) != None:
                cur = cur.children[char]
            else:
                prev = cur
                cur = TrieNode()
                prev.children[char] = cur

        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for char in word:
            if cur.children.get(char, None) != None:
                cur = cur.children[char]
            else:
                return False
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            if cur.children.get(char, None) != None:
                cur = cur.children[char]
            else:
                return False
        return True
