# title: sum-of-unique-elements
# detail: https://leetcode.com/submissions/detail/452740131/
# datetime: Sat Feb  6 22:33:18 2021
# runtime: 48 ms
# memory: 14 MB

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum(k for k, v in collections.Counter(nums).items() if v == 1)