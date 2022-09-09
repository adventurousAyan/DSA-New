# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """


class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """

        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def f(x, y, d):

            robot.clean()

            directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

            for i in range(4):
                new_d = (d + i) % 4
                nx, ny = x + directions[new_d][0], y + directions[new_d][1]
                if (nx, ny) not in seen and robot.move():
                    seen.add((nx, ny))
                    f(nx, ny, new_d)
                    go_back()
                robot.turnRight()

        seen = set()
        seen.add((0, 0))
        f(0, 0, 0)
