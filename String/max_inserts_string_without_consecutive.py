class Solution:
    # https://algo.monster/problems/max_inserts_to_obtain_string_without_3_consecutive_a
    def maxInserts(self, s: str) -> int:

        n = len(s)
        a_count = 0
        other_count = 0
        for i in range(n):
            if s[i] == "a":
                a_count += 1
            else:
                other_count += 1
                a_count = 0

            if a_count == 3:
                return -1
        return 2 * (other_count + 1) - (n - other_count)


s = Solution()
print(s.maxInserts("baaaa"))
