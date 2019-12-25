# title: longest-palindromic-subsequence
# detail: https://leetcode.com/submissions/detail/286780659/
# datetime: Wed Dec 18 11:46:32 2019
# runtime: 836 ms
# memory: 224.5 MB

from functools import lru_cache
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @lru_cache(None)
        def find(i, j):
            if i == j:
                return 1
            if i > j:
                return 0
            if s[i] == s[j]:
                return find(i + 1, j - 1) + 2
            return max(find(i + 1, j), find(i, j - 1))
        return find(0, len(s) - 1)