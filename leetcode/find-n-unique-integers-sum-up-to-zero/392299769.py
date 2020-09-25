# title: find-n-unique-integers-sum-up-to-zero
# detail: https://leetcode.com/submissions/detail/392299769/
# datetime: Mon Sep  7 21:48:52 2020
# runtime: 28 ms
# memory: 13.9 MB

class Solution:
    def sumZero(self, n: int) -> List[int]:
        return [j * (i + 1) for i in range(n // 2) for j in [-1, 1]] + ([0] if n % 2 else [])
            