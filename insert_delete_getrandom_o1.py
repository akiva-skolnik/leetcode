import random


# https://leetcode.com/problems/insert-delete-getrandom-o1
class RandomizedSet:

    def __init__(self):
        self.data = []
        self.mapping = {}  # between vals and indexes

    def insert(self, val: int) -> bool:
        if val in self.mapping:
            return False
        self.data.append(val)
        self.mapping[val] = len(self.data) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.mapping:
            return False
        i = self.mapping[val]
        self.mapping.pop(self.data[i])
        last_val = self.data.pop()
        if i < len(self.data):
            self.data[i] = last_val
            self.mapping[last_val] = i
        return True

    def getRandom(self) -> int:
        return random.choice(self.data)


def test():
    randomized_set = RandomizedSet()
    assert randomized_set.insert(1) is True
    assert randomized_set.remove(2) is False
    assert randomized_set.insert(2) is True
    val = randomized_set.getRandom()
    assert val in [1, 2]
    other_val = 1 if val == 2 else 2
    assert randomized_set.remove(val) is True
    assert randomized_set.insert(other_val) is False
    assert randomized_set.getRandom() == other_val
