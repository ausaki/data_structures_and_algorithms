# title: split-a-string-into-the-max-number-of-unique-substrings
# detail: https://leetcode.com/submissions/detail/399148179/
# datetime: Tue Sep 22 18:00:55 2020
# runtime: 336 ms
# memory: 14.1 MB

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        strs = set()
        def split(i):
            if i == n:
                return len(strs)
            m = 0
            for j in range(i, n):
                t = s[i:j + 1]
                if t not in strs:
                    strs.add(t)
                    m = max(m, split(j + 1))
                    strs.remove(t)
            return m
        
        return split(0)