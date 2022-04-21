class Solution:
    # Function to check if the linked list has a loop.
    def detectLoop(self, head):
        # code here
        cur_node = head
        fast = cur_node
        slow = cur_node
        isloop = False
        prev = cur_node
        while slow.next and fast.next and fast.next.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                isloop = True
                break

        return isloop
