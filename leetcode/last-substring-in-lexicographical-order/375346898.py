# title: last-substring-in-lexicographical-order
# detail: https://leetcode.com/submissions/detail/375346898/
# datetime: Mon Aug  3 17:10:37 2020
# runtime: 384 ms
# memory: 17.3 MB

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
            for j in range(1, min(start - i + 1, N - start)):
                if s[i + j] < s[start + j]:
                    break
                if s[i + j] > s[start + j]:
                    start = i
                    break
            else:
                start = i
        return s[start:]