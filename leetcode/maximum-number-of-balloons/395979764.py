# title: maximum-number-of-balloons
# detail: https://leetcode.com/submissions/detail/395979764/
# datetime: Tue Sep 15 15:00:29 2020
# runtime: 32 ms
# memory: 14 MB

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = dict.fromkeys('balon', 0)
        for c in text:
            if c in d:
                d[c] += 1
        d['l'] //= 2
        d['o'] //= 2
        return min(d.values())