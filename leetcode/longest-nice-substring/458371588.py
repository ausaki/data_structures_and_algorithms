# title: longest-nice-substring
# detail: https://leetcode.com/submissions/detail/458371588/
# datetime: Sat Feb 20 22:41:48 2021
# runtime: 184 ms
# memory: 14.2 MB

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)
        max_len = 0
        pos = -1
        for i in range(n):
            a = set()
            b = set()
            for j in range(i, n):
                if s[j].islower():
                    a.add(s[j])
                else:
                    b.add(s[j])
                if set(c.upper() for c in a) == b:
                    l = j - i + 1
                    if l > max_len:
                        max_len = l
                        pos = i
        return s[pos:pos + max_len]
                
                        