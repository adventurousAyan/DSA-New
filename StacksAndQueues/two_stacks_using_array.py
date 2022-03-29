# Function to push an integer into the stack1.
top3 = -2
top4 = -1


def push1(a, x):
    # code here

    global top3
    top3 = top3 + 2
    a[top3] = x


# Function to push an integer into the stack2.
def push2(a, x):
    # code here
    global top4
    top4 = top4 + 2
    a[top4] = x


# Function to remove an element from top of the stack1.
def pop1(a):
    # code here

    global top3
    if len(a) > 0 and top3 != -2:
        val = a[top3]
        top3 = top3 - 2
        return val
    else:
        return -1


# Function to remove an element from top of the stack2.
def pop2(a):
    # code here
    global top4
    if len(a) > 0 and top4 != -1:
        val = a[top4]
        top4 = top4 - 2
        return val
    else:
        return -1
