class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None

    def insert(self, start, end):
        if end <= self.start:
            if self.left:
                return self.left.insert(start, end)
            else:
                self.left = Node(start, end)
                return True
        elif start >= self.end:
            if self.right:
                return self.right.insert(start, end)
            else:
                self.right = Node(start, end)
                return True
        else:
            return False


class MyCalendar:
    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:

        if self.root is None:
            self.root = Node(start, end)
            return True
        else:
            return self.root.insert(start, end)
