"""Return reference of new head of the reverse linked list
  The input list will have at least one element
  Node is defined as

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
  This is method only submission.
  You only need to complete the method.
"""


class Solution:
    def reverse(self, head, k):
        # Code here
        if head is None:
            return None
        else:
            cur1 = head
            cur2 = head.next
            reversed_list = cur1
            cnt = 0

            while cnt != k - 1 and cur2:
                tmp = cur2
                cur2 = cur2.next
                tmp.next = reversed_list
                reversed_list = tmp
                cnt += 1

            cur1.next = self.reverse(cur2, k)
            return reversed_list
