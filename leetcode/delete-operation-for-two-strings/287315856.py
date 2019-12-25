# title: delete-operation-for-two-strings
# detail: https://leetcode.com/submissions/detail/287315856/
# datetime: Fri Dec 20 17:50:52 2019
# runtime: 476 ms
# memory: 63.6 MB

from functools import lru_cache
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @lru_cache(None)
        def edit(i, j):
            if i == -1:
                return j + 1
            if j == -1:
                return i + 1
            d = min(edit(i - 1, j), edit(i, j - 1)) + 1
            if word1[i] == word2[j]:
                d = min(d, edit(i - 1, j - 1))
            return d
        
        N1, N2 = len(word1), len(word2)
        return edit(N1 - 1, N2 - 1)