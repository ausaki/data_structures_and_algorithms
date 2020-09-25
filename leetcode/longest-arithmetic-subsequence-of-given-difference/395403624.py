# title: longest-arithmetic-subsequence-of-given-difference
# detail: https://leetcode.com/submissions/detail/395403624/
# datetime: Mon Sep 14 11:50:41 2020
# runtime: 716 ms
# memory: 27 MB

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        seq = {}
        m = 0
        for a in arr:
            b = max(seq.get(a, 0), seq.pop(a - difference, 0) + 1)
            seq[a] = b
            m = max(m, b)
        return m