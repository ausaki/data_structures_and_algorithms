# title: count-odd-numbers-in-an-interval-range
# detail: https://leetcode.com/submissions/detail/376869299/
# datetime: Thu Aug  6 15:28:07 2020
# runtime: 32 ms
# memory: 13.8 MB

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 == 0:
            low += 1
        return 1 + (high - low) // 2