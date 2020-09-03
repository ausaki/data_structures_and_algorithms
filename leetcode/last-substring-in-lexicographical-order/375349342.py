# title: last-substring-in-lexicographical-order
# detail: https://leetcode.com/submissions/detail/375349342/
# datetime: Mon Aug  3 17:20:07 2020
# runtime: 976 ms
# memory: 17.2 MB

class Solution:
    def lastSubstring(self, s: str) -> str:
        N = len(s)
        start = N - 1
        for i in reversed(range(N - 1)):
            if s[i] < s[start]:
                continue
            if s[i] > s[start]:
                start = i
                continue
            j = min(start - i + 1, N - start)
            if s[i: i + j] >= s[start: start + j]:
                start = i
        return s[start:]