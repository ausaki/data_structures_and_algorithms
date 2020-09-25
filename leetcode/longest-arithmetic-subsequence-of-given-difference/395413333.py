# title: longest-arithmetic-subsequence-of-given-difference
# detail: https://leetcode.com/submissions/detail/395413333/
# datetime: Mon Sep 14 12:13:09 2020
# runtime: 696 ms
# memory: 26.8 MB

class Solution:
    def longestSubsequence(self, arr: List[int], diff: int) -> int:
        res = {}
        for num in arr:
            res[num] = res[num - diff] + 1 if (num - diff) in res else 1
        return max(res.values())