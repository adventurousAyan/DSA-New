class Solution:
    # Function to delete a node without any reference to head pointer.
    def deleteNode(self, curr_node):
        # code here
        next_node = curr_node.next
        curr_node.data = next_node.data
        curr_node.next = next_node.next
