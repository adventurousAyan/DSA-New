# https://leetcode.com/problems/reverse-string/submissions/
def reverse_array(arr):
    ls = []
    for a in range(len(arr) - 1, -1, -1):
        ls.append(arr[a])
    return ls


def reverse_array__without_extra_space(arr):
    lp = 0
    rp = len(arr) - 1
    while lp <= rp:
        arr[lp], arr[rp] = arr[rp], arr[lp]
        lp = lp + 1
        rp = rp - 1
    return arr


# arr = [4,5,1,2]
# print(reverse_array(arr))


arr = [4, 5, 1, 2]
print(reverse_array__without_extra_space(arr))
