from typing import List

# N Array Tree
class Node:
    def __init__(self, child_edges: List["Edge"] = None) -> None:
        self.child_edges = child_edges or []


class Edge:
    def __init__(self, cost: int, target: "Node") -> None:
        self.cost = cost
        self.target = target


def find_min_cost_leaf(root: "Node") -> "Node":
    # Write solution here

    def dfs(root, su):

        # Base Case:
        if root is None:
            return root
        # This is a leaf node
        if len(root.child_edges) == 0:
            if su < mini:
                mini = su
                min_node = root
        # Traverse through the child edges
        for edge in root.child_edges:
            # Check if the value is more, we donot need to traverse the tree
            if su + edge.cost < mini:
                dfs(edge.target, su + edge.cost)

    mini = float("inf")
    min_node = None
    dfs(root, 0)
    return min_node
