import queue

from queue import Queue
import queue
from sys import maxsize

d = {}

d[1] = [2, 3]
d[2] = [1, 3, 4]
d[3] = [1, 2, 5]
d[4] = [2, 5]
d[5] = [3, 4]

print(d)
d1 = {}
for key in d.keys():
    d1[key] = -1


def bfs(source, dest):
    visited = []
    queue = Queue(maxsize=5)

    queue.put(source)
    visited.append(source)
    d1[source] = -1
    while not queue.empty():

        val = queue.get()
        print(val)
        if val == dest:
            break
        for item in d.get(val):
            if not item in visited:
                d1[item] = val
                queue.put(item)
                visited.append(item)
    # print(d1)
    return d1


print(bfs(1, 5))
