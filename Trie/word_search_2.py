# https://leetcode.com/problems/word-search-ii/

from typing import List

# For intuition # https://www.youtube.com/watch?v=asbcE9mZz_U

# Trie Node class
class TrieNode:
    def __init__(self):
        self.children = {}
        self.terminal = False


# Trie class
class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Add words to Trie
    def add_word(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.terminal = True

    # Prune words from Trie
    def prune_word(self, word) -> None:
        cur = self.root
        node_child_key: list[tuple[TrieNode, str]] = []
        for char in word:
            node_child_key.append((cur, char))
            cur = cur.children[char]
        for par_node, child_key in reversed(node_child_key):
            target_node = par_node.children[child_key]
            if len(target_node.children) == 0:
                del par_node.children[child_key]
            else:
                return


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        # Declare a Trie
        trie = Trie()

        # Add all words in Trie
        for word in words:
            trie.add_word(word)

        # Is valid condition
        def is_valid(r, c):
            return r >= 0 and r < m and c >= 0 and c < n and board[r][c]

        def dfs(r, c, node, w1):

            # Trie donot contain the value contained in cell. Hence return
            if board[r][c] not in node.children:
                return
            # Value is present in Trie, hence get the node
            node = node.children.get(board[r][c])
            # Apped the board[r][c] to w1
            w1 += board[r][c]
            # If we reached a leaf node, that means we found word
            # Add it to result and also we need to delete from Trie, else it will give TLE
            if node.terminal:
                res.add(w1)
                node.terminal = False
                trie.prune_word(w1)

            tmp = board[r][c]
            board[r][c] = None

            # Recursive DFS Implementation
            directions = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
            for nr, nc in directions:
                if is_valid(nr, nc):
                    dfs(nr, nc, node, w1)
            # Back Tracking
            board[r][c] = tmp

        m, n = len(board), len(board[0])
        res = set()
        # Loop through each cell and do dfs
        for i in range(m):
            for j in range(n):
                dfs(i, j, trie.root, "")
        return list(res)
