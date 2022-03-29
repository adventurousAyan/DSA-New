def reverse(S):
    # Add code here
    ls = list(S)
    return reverse_string(ls, "")


def reverse_string(ls, str1):
    if len(ls) == 0:
        # print(str1)
        return str1
    else:
        val = ls.pop()
        str1 = str1 + val
        return reverse_string(ls, str1)
