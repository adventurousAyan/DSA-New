from typing import List

# https://leetcode.com/problems/daily-temperatures/

# Both solutions are correct


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []

        n = len(temperatures)
        ls = [0] * n
        for i in range(n - 1, -1, -1):

            while len(stack) > 0 and stack[-1][1] <= temperatures[i]:
                stack.pop()

            if len(stack) > 0 and stack[-1][1] > temperatures[i]:
                ls[i] = stack[-1][0] - i

            stack.append((i, temperatures[i]))

        return ls


#################### 2nd Approach ########################################


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []

        n = len(temperatures)
        ans = [0] * n
        for i in range(n - 1, -1, -1):

            while len(stack) > 0 and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()

            if len(stack) > 0 and temperatures[stack[-1]] > temperatures[i]:
                ans[i] = stack[-1] - i

            stack.append(i)

        return ans


######################3rd Approach ################################


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []

        n = len(temperatures)
        ans = [0] * n
        for i in range(n):

            while len(stack) > 0 and temperatures[stack[-1]] < temperatures[i]:
                idx = stack.pop()
                ans[idx] = i - idx

            stack.append(i)

        return ans
