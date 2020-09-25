# title: longest-arithmetic-subsequence-of-given-difference
# detail: https://leetcode.com/submissions/detail/395406614/
# datetime: Mon Sep 14 11:57:29 2020
# runtime: 1004 ms
# memory: 27.3 MB

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        seq = {}
        m = 0
        for a in arr:
            b = max(seq.get(a, 0), seq.pop(a - difference, 0) + 1)
            seq[a] = b
            m = max(m, b)
        return m