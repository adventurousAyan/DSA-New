d = {}

d[1] = [2, 3]
d[2] = [1, 3, 4]
d[3] = [1, 2, 5]
d[4] = [2, 5]
d[5] = [3, 4]

print(d)


def dfs(source, dest):
    visited = []
    arr = []
    result = False
    visited.append(source)
    arr.append(source)
    while len(arr) != 0:
        val = arr.pop()
        if val == dest:
            result = True
            break
        for item in d.get(val):
            if not item in visited:
                visited.append(item)
                arr.append(item)
    print(visited)
    return result


print(dfs(1, 5))
