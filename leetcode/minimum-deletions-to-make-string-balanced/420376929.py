# title: minimum-deletions-to-make-string-balanced
# detail: https://leetcode.com/submissions/detail/420376929/
# datetime: Sun Nov 15 11:45:14 2020
# runtime: 484 ms
# memory: 15 MB

class Solution:
    def minimumDeletions(self, s: str) -> int:
        ta = s.count('a')
        a, b = 0, 0
        j = -1
        ans = len(s)
        for i, c in enumerate(s):
            if c == 'a':
                if j >= 0:
                    l = i - j
                    ans = min(ans, b + ta - a)
                    b += l
                a += 1
                j = -1
                continue
            if j == -1:
                j = i
        ans = min(ans, b)
        return ans
        