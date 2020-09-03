# title: last-substring-in-lexicographical-order
# detail: https://leetcode.com/submissions/detail/375363847/
# datetime: Mon Aug  3 18:19:39 2020
# runtime: 264 ms
# memory: 17 MB

class Solution:
    def lastSubstring(self, s: str) -> str:
        i, j, k = 0, 1, 0
        n = len(s)
        while j + k < n:
            if s[i+k] == s[j+k]:
                k += 1
                continue
            elif s[i+k] > s[j+k]:
                j = j + k + 1
            else:
                i = max(i + k + 1, j)
                j = i + 1
            k = 0
        return s[i:]
