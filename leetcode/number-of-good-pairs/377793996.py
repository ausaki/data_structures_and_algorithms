# title: number-of-good-pairs
# detail: https://leetcode.com/submissions/detail/377793996/
# datetime: Sat Aug  8 17:00:14 2020
# runtime: 28 ms
# memory: 13.8 MB

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return sum(cnt * (cnt - 1) // 2 for cnt in collections.Counter(nums).values())
