from typing import List


class Solution:
    # https://leetcode.com/problems/evaluate-reverse-polish-notation/

    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        operands = ["+", "-", "*", "/"]
        for val in tokens:
            if val in operands:
                val1 = stack.pop()
                val2 = stack.pop()
                val = str(int(eval(val2 + val + val1)))
            stack.append(val)
        return stack.pop()
