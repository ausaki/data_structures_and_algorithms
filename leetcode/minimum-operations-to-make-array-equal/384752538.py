# title: minimum-operations-to-make-array-equal
# detail: https://leetcode.com/submissions/detail/384752538/
# datetime: Sun Aug 23 01:47:51 2020
# runtime: 56 ms
# memory: 13.5 MB

class Solution:
    def minOperations(self, n: int) -> int:
        if n % 2:
            return (n ** 2 - 1) // 4
        return n ** 2 // 4
        