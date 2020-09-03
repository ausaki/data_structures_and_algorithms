# title: minimum-operations-to-make-array-equal
# detail: https://leetcode.com/submissions/detail/384752835/
# datetime: Sun Aug 23 01:48:40 2020
# runtime: 56 ms
# memory: 13.7 MB

class Solution:
    def minOperations(self, n: int) -> int:
        return ((n ** 2) - (n % 2)) // 4
        