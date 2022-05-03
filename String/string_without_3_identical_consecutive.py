class Solution:

    # https://algo.monster/problems/string_without_3_identical_consecutive_letters

    def filterString(self, s: str) -> int:

        stack = []
        n = len(s)
        for i in range(n - 1, -1, -1):
            stack.append(s[i])

        prev = ""
        count = 0
        s1 = ""
        while not len(stack) == 0:
            val = stack.pop()
            if prev == val:
                count += 1
            else:
                count = 0
            prev = val
            if count >= 0 and count <= 1:
                s1 += val
        return s1


s = Solution()
print(s.filterString("uuuuxaaaaxum"))
