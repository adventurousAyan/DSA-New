class Solution:

    # https://leetcode.com/problems/plus-one/

    def plusOne(self, digits: List[int]) -> List[int]:

        q = deque()
        carry = 0
        n = len(digits)
        ls = [0] * n
        ls[n - 1] = 1
        for i in range(n - 1, -1, -1):
            q.appendleft((digits[i] + carry + ls[i]) % 10)
            carry = (digits[i] + carry + ls[i]) // 10

        if carry != 0:
            q.appendleft(carry)
        return q
