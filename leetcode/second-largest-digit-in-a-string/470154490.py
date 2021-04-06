# title: second-largest-digit-in-a-string
# detail: https://leetcode.com/submissions/detail/470154490/
# datetime: Sat Mar 20 22:32:20 2021
# runtime: 48 ms
# memory: 14.3 MB

class Solution:
    def secondHighest(self, s: str) -> int:
        d = sorted(set(c for c in s if c.isdigit()))
        n = len(d)
        if n < 2:
            return -1
        return d[-2]