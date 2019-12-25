# title: insert-delete-getrandom-o(1)
# detail: https://leetcode.com/submissions/detail/285238705/
# datetime: Wed Dec 11 18:41:32 2019
# runtime: 84 ms
# memory: 16.8 MB

import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.array = []
        self.dict = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.dict:
            return False
        self.array.append(val)
        self.dict[val] = len(self.array) - 1
        return True
    
    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.dict:
            return False
        index = self.dict.pop(val)
        if index != len(self.array) - 1:
            val = self.array.pop()
            self.array[index] = val
            self.dict[val] = index
        else:
            self.array.pop()
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        if not self.array:
            return -1
        return random.choice(self.array)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()