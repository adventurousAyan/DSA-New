class Solution:
    def isValid(self, s: str) -> bool:

        st = []
        open_braces = ["[", "{", "("]
        for ch in s:
            if ch in open_braces:
                st.append(ch)
            else:
                if len(st) > 0:
                    top = st[-1]
                    item = ch
                    if ((top == "[" and item == "]") or (top == "{" and item == "}") or  (top == "(" and item == ")")):
                        st.pop()
                    else:
                        st.append(ch)
                else:
                    return False
        return len(st) == 0

        



        