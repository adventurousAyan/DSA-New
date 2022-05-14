# You're developing a system for scheduling advising meetings with students in a Computer Science program. Each meeting should be scheduled when a student
# has completed 50% of their academic program.

# Each course at our university has at most one prerequisite that must be taken first. No two courses share a prerequisite. There is only one path through the program.

# Write a function that takes a list of (prerequisite, course) pairs, and returns the name of the course that the student will be taking
# when they are halfway through their program. (If a track has an even number of courses, and therefore has two "middle" courses, you should return the first one.)

# Sample input 1: (arbitrarily ordered)
# prereqs_courses1 = [
#   ["Foundations of Computer Science", "Operating Systems"],
#   ["Data Structures", "Algorithms"],
#   ["Computer Networks", "Computer Architecture"],
#   ["Algorithms", "Foundations of Computer Science"],
#   ["Computer Architecture", "Data Structures"],
#   ["Software Design", "Computer Networks"]
# ]

# In this case, the order of the courses in the program is:
#   Software Design
#   Computer Networks
#   Computer Architecture
#   Data Structures
#   Algorithms
#   Foundations of Computer Science
#   Operating Systems

# Sample output 1:
#   "Data Structures"

# Sample input 2:
# prereqs_courses2 = [
#     ["Algorithms", "Foundations of Computer Science"],
#     ["Data Structures", "Algorithms"],
#     ["Foundations of Computer Science", "Logic"],
#     ["Logic", "Compilers"],
#     ["Compilers", "Distributed Systems"],
# ]

# Sample output 2:
#   "Foundations of Computer Science"

# Sample input 3:
# prereqs_courses3 = [
#   ["Data Structures", "Algorithms"],
# ]

# Sample output 3:
#   "Data Structures"

# Complexity analysis variables:

# n: number of pairs in the input


def order_courses(prereqs_courses1):

    adj = {}
    s = set()

    for val in prereqs_courses1:
        s.add(val[0])
        s.add(val[1])

    courses = list(s)

    for val in prereqs_courses1:
        adj[val[0]] = adj.get(val[0], []) + [val[1]]

    n = len(adj.keys())

    visited = {}

    for course in courses:
        visited[course] = -1
    l1 = []

    for course in courses:
        res = dfs(adj, visited, course, [])
        if res is not None:
            if len(l1) == 0:
                l1 = res
            else:
                if adj[res[0]] == l1[0]:
                    l1 = l1 + res
                else:
                    l1 = res + l1
    start = 0
    end = len(courses) - 1
    mid = start + (end - start) // 2
    return l1[mid]


def dfs(adj, visited, course, ls):
    if visited[course] == 1:
        return

    neigh = adj.get(course, [])

    visited[course] = 1
    ls.append(course)
    for n in neigh:
        dfs(adj, visited, n, ls)

    return ls


res = order_courses(
    [
        ["Foundations of Computer Science", "Operating Systems"],
        ["Data Structures", "Algorithms"],
        ["Computer Networks", "Computer Architecture"],
        ["Algorithms", "Foundations of Computer Science"],
        ["Computer Architecture", "Data Structures"],
        ["Software Design", "Computer Networks"],
    ]
)

print(res)
