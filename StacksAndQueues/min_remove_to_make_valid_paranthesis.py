# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        stack = []

        s = list(s)
        for i in range(len(s)):
            s1 = s[i]
            # If opening bracket, put it into stack
            if s1 == "(":
                stack.append((s1, i))
            # If closing bracket, check if top of stack contains a open bracket. If yes, pop from stack
            # Else, that means it has redundant ")" which needs to be removed. So set it to blank
            if s1 == ")":
                if len(stack) > 0 and stack[-1][0] == "(":
                    stack.pop()
                else:
                    s[i] = ""

        # This is the case where it may contain a redundant open bracket. In this case, we need to remove
        # this as well by setting blank
        while stack:
            s2, i = stack.pop()
            s[i] = ""

        return "".join(s)
