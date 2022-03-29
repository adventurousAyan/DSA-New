# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
    You may assume the two numbers do not contain any leading zero, except the number 0 itself.
    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
    """

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        ls1 = []
        ls2 = []

        while l1 is not None:
            ls1.append(l1.val)
            l1 = l1.next

        while l2 is not None:
            ls2.append(l2.val)
            l2 = l2.next

        l1 = len(ls1)
        l2 = len(ls2)
        res = []
        if l1 > l2:
            diff = l1 - l2
            while diff > 0:
                ls2.append(0)
                diff = diff - 1
        if l2 > l1:
            diff = l2 - l1
            while diff > 0:
                ls1.append(0)
                diff = diff - 1
        l1 = len(ls1)
        l2 = len(ls2)
        print(ls1)
        print(ls2)
        if l1 == l2:
            count = 0
            car = 0
            while count < len(ls1):
                s1 = int((ls1[count] + ls2[count] + car) % 10)
                # val = s1 + car
                res.append(s1)
                car = int((ls1[count] + ls2[count] + car) / 10)
                count = count + 1
            if car != 0:
                res.append(car)
        ls = ListNode(res[0])
        head = ls
        for x in range(1, len(res)):
            l1 = ListNode(res[x])
            ls.next = l1
            ls = l1
        return head
