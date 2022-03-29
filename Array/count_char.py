def count_char_2(input):
    s1 = ""
    s = list(input)
    prev = input[0]
    cnt = 1
    ls = []
    ls.append(prev)

    for i in range(1, len(input)):

        if prev == s[i]:
            ls.pop()
            cnt += 1
            # s[i] = f"{cnt}{s[i]}"
            ls.append(f"{cnt}{prev}")
        else:
            #   s1 = s1 + f"{val}"
            cnt = 1
            prev = s[i]
            ls.append(prev)

    return "".join(ls)


print(count_char_2("abcccaad"))
