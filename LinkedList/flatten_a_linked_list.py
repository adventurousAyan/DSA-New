# User function Template for python3


"""

class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
"""

# https://practice.geeksforgeeks.org/problems/flattening-a-linked-list/1


def flatten(root):
    # Your code here
    if root is None:
        return None

    rh = flatten(root.next)

    if rh is None:
        return root
    else:
        dummy = Node(0)
        cur = dummy
        l1 = root
        l2 = rh
        while l1 is not None and l2 is not None:
            if l1.data <= l2.data:
                cur.bottom = Node(l1.data)
                l1 = l1.bottom
            elif l1.data > l2.data:
                cur.bottom = Node(l2.data)
                l2 = l2.bottom
            cur = cur.bottom

        while l1 is not None:
            cur.bottom = Node(l1.data)
            l1 = l1.bottom
            cur = cur.bottom
        while l2 is not None:
            cur.bottom = Node(l2.data)
            l2 = l2.bottom
            cur = cur.bottom
        return dummy.bottom
