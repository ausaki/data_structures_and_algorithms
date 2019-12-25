# title: delete-operation-for-two-strings
# detail: https://leetcode.com/submissions/detail/287315965/
# datetime: Fri Dec 20 17:51:49 2019
# runtime: 256 ms
# memory: 29.9 MB

from functools import lru_cache
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @lru_cache(None)
        def edit(i, j):
            if i == -1:
                return j + 1
            if j == -1:
                return i + 1
            if word1[i] == word2[j]:
                d = edit(i - 1, j - 1)
            else:
                d = min(edit(i - 1, j), edit(i, j - 1)) + 1
            return d
        
        N1, N2 = len(word1), len(word2)
        return edit(N1 - 1, N2 - 1)