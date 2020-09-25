# title: longest-arithmetic-subsequence-of-given-difference
# detail: https://leetcode.com/submissions/detail/395402971/
# datetime: Mon Sep 14 11:49:08 2020
# runtime: 944 ms
# memory: 27 MB

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        seq = {}
        for a in arr:
            seq[a] = max(seq.get(a, 0), seq.pop(a - difference, 0) + 1)
        return max(seq.values())