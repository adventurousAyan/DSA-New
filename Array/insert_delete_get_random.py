# https://leetcode.com/problems/insert-delete-getrandom-o1/


import random


class RandomizedSet:
    def __init__(self):
        self.d1 = {}

    def insert(self, val: int) -> bool:
        if val not in self.d1:
            self.d1[val] = 1
            return True
        self.d1[val] += 1

        return False

    def remove(self, val: int) -> bool:
        if val in self.d1:
            del self.d1[val]
            return True
        return False

    def getRandom(self) -> int:
        ls = list(self.d1.keys())
        idx = random.randint(0, len(ls) - 1)
        return ls[idx]


################2nd Approach #########################################


class RandomizedSet:
    def __init__(self):
        # Declare an array and dict
        self.d1 = {}
        self.num_list = []

    def insert(self, val: int) -> bool:
        if val not in self.d1:
            # If val is not in dict, store val in the dict with key being val and value being
            # the index at which it is stored
            self.d1[val] = len(self.num_list)
            self.num_list.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.d1:
            # Get the index from dict
            idx = self.d1[val]
            # Get the last value from list
            last_val = self.num_list[-1]
            # Replace the value with the last val calculated earlier
            self.num_list[idx] = last_val
            # Delete the lastval from list
            self.num_list.pop()
            # Also update lastVal index in dict to proper index
            self.d1[last_val] = idx
            # Delete val from dict
            del self.d1[val]
            return True
        return False

    def getRandom(self) -> int:
        # Return random number present in array
        return random.choice(self.num_list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
