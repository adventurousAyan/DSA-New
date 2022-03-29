def print_nos(n):
    ls = []
    arr = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    print_excel_nos(arr, n, ls)
    return ls


def print_excel_nos(arr, n, ls):
    t = []
    if n == 0:
        return ls
    else:
        if len(ls) == 0:
            for a in arr:
                ls.append(a)
        else:
            for a in ls:
                for b in arr:
                    t.append(a + b)
    ls.extend(t)
    print_excel_nos(arr, n - 1, ls)


print(print_nos(3))
