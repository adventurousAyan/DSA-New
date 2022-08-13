from typing import List


class Codec:
    # https://leetcode.com/problems/encode-and-decode-strings/

    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        s = "#"
        for s1 in strs:
            for i in range(len(s1)):
                val = ord(s1[i])
                val = str(val)
                if i == len(s1) - 1:
                    s += val
                else:
                    s += val + ","
            s += "#"
        return s

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        ls = []
        l1 = s.split("#")
        for i in range(1, len(l1) - 1):
            s1 = ""
            if l1[i] != "":
                for val in l1[i].split(","):
                    val = int(val)
                    s1 += chr(val)
            ls.append(s1)
        return ls
