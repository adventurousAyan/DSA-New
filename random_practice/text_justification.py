from typing import List

# https://leetcode.com/problems/text-justification/


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        ls = []

        cur_line = []
        width = 0

        i = 0

        while i < len(words):
            cur_word = words[i]
            if len(cur_word) + width <= maxWidth:
                cur_line.append(cur_word)
                width += len(cur_word) + 1
                i += 1
            else:
                spaces = maxWidth - width + len(cur_line)
                added = 0
                j = 0

                while added < spaces:
                    if j >= len(cur_line) - 1:
                        j = 0
                    cur_line[j] += " "
                    j += 1
                    added += 1

                ls.append("".join(cur_line))
                cur_line = []
                width = 0

        # For Last word
        res = " ".join(cur_line)
        res += " " * (maxWidth - len(res))
        ls.append(res)

        return ls
