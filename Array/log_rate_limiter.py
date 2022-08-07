# https://leetcode.com/problems/logger-rate-limiter/
class Logger:
    def __init__(self):
        self.d1 = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.d1:
            self.d1[message] = timestamp + 10
            return True
        else:
            if timestamp >= self.d1[message]:
                self.d1[message] = timestamp + 10
                return True
            else:
                return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
