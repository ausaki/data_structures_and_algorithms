# title: replace-the-substring-for-balanced-string
# detail: https://leetcode.com/submissions/detail/282245374/
# datetime: Thu Nov 28 16:40:42 2019
# runtime: 464 ms
# memory: 13.4 MB

from functools import lru_cache

class Solution:
    def balancedString(self, s: str) -> int:
        count = collections.Counter(s)
        res = n = len(s)
        i = 0
        for j, c in enumerate(s):
            count[c] -= 1
            while i < n and all(n / 4 >= count[c] for c in 'QWER'):
                res = min(res, j - i + 1)
                count[s[i]] += 1
                i += 1
        return res
