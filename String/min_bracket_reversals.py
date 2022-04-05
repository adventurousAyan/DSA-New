def countRev(s):
    # your code here

    n = len(s)
    ans = 0
    if n % 2 != 0:
        return -1
    else:
        op = 0
        for val in s:
            if val == "{":
                op += 1
            elif val == "}":
                if op > 0:
                    op -= 1
                else:
                    op += 1
                    ans += 1

        return op // 2 + ans
