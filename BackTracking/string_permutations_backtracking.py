# User function Template for python3


class Solution:
    def find_permutation(self, S):
        # Code here
        ls = []
        return self.solve(S, 0, ls)

    def solve(self, s1, j, ls):
        if len(s1) == j:
            ls.append(s1)
        else:
            for i in range(j, len(s1)):
                s1 = self.swap(s1, i, j)
                self.solve(s1, j + 1, ls)
                s1 = self.swap(s1, i, j)
        return sorted(ls)

    def swap(self, s1, i, j):
        s2 = list(s1)
        s2[i], s2[j] = s2[j], s2[i]
        return "".join(s2)
