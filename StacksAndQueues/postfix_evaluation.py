class Solution:

    # Function to evaluate a postfix expression.
    def evaluatePostfix(self, S):
        # code here

        ls = ["*", "/", "+", "-"]
        s = []

        for a in S:
            if a not in ls:
                s.append(a)
            else:
                val1 = s.pop()
                val2 = s.pop()
                val = int(eval(str(val2) + a + str(val1)))
                s.append(val)

        res = s.pop()
        return res
