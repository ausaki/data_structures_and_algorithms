# title: longest-arithmetic-subsequence-of-given-difference
# detail: https://leetcode.com/submissions/detail/395403354/
# datetime: Mon Sep 14 11:50:06 2020
# runtime: 1008 ms
# memory: 27 MB

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        seq = {}
        m = 0
        for a in arr:
            seq[a] = max(seq.get(a, 0), seq.pop(a - difference, 0) + 1)
            m = max(m, seq[a])
        return m