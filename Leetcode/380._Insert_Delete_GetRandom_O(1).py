import random


class RandomizedSet:

    def __init__(self):

        self.nums = []

        self.indexes = {}

    def insert(self, val: int) -> bool:

        if val in self.indexes:
            return False

        self.nums.append(val)

        self.indexes[val] = len(self.nums) - 1

        return True

    def remove(self, val: int) -> bool:
        if val not in self.indexes:
            return False
        idx = self.indexes[val]

        last_val = self.nums[-1]

        self.nums[idx] = last_val

        self.indexes[last_val] = idx
        self.nums.pop()

        del self.indexes[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)
