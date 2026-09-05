class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        oper = ["+", "-", "*", "/"]

        for t in tokens:
            if t not in oper:
                st.append(t)
            else:
                val1 = st.pop()
                val2 = st.pop()
                expr = eval(val2 + t + val1)
                if t == "/":
                    st.append(str(int(expr)))
                else:
                    st.append(str(expr))
        return int(st[-1])