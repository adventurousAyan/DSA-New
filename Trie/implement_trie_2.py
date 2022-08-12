class TrieNode:

    # https://leetcode.com/problems/implement-trie-ii-prefix-tree/

    def __init__(self):
        self.children = {}
        self.terminal = False
        self.wc = 0  # Prefix word count
        self.fc = 0  # Full word count


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for ch in word:

            if not cur.children.get(ch):
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
            cur.wc += 1

        cur.terminal = True
        cur.fc += 1

    def countWordsEqualTo(self, word: str) -> int:

        cur = self.root
        for ch in word:
            if not cur.children.get(ch):
                return 0
            cur = cur.children[ch]

        return cur.fc

    def countWordsStartingWith(self, prefix: str) -> int:
        cur = self.root

        for ch in prefix:
            if not cur.children.get(ch):
                return 0
            cur = cur.children[ch]
        return cur.wc

    def erase(self, word: str) -> None:
        cur = self.root

        for ch in word:
            if cur.children.get(ch):
                cur = cur.children[ch]
                cur.wc -= 1

        cur.fc -= 1


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)
