class Solution:
    """Given a string s, find the length of the longest substring without repeating characters.
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        map = {}
        max = float("-inf")
        if s == "":
            return 0
        while i <= j and j < len(s):
            val = s[j]
            if val in map:
                map.pop(s[i])
                i = i + 1
                j = j - 1
            else:
                map[val] = 1
            cout = j - i + 1
            if cout > max:
                max = cout
            j = j + 1

        return max
