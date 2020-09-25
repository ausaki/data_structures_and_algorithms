# title: longest-arithmetic-subsequence-of-given-difference
# detail: https://leetcode.com/submissions/detail/395412507/
# datetime: Mon Sep 14 12:11:16 2020
# runtime: 924 ms
# memory: 27 MB

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        mi = min(arr)
        seq = [0] * (max(arr) - mi + 1)
        m = 0
        for a in arr:
            b = a - difference - mi
            v = 1
            if 0 <= b < len(seq):
                v += seq[b]
                seq[b] = 0
            seq[a - mi] = max(seq[a - mi], v)
            m = max(m, seq[a - mi])
        return m