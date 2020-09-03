# title: count-odd-numbers-in-an-interval-range
# detail: https://leetcode.com/submissions/detail/376869808/
# datetime: Thu Aug  6 15:29:19 2020
# runtime: 36 ms
# memory: 13.8 MB

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return 1 + (high - (low + 1 - low % 2)) // 2