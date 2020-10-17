# title: stamping-the-sequence
# detail: https://leetcode.com/submissions/detail/403903738/
# datetime: Sat Oct  3 21:09:49 2020
# runtime: 200 ms
# memory: 14.3 MB

class Solution:
    def movesToStamp(self, s, t):
        n, m, t, s, res = len(t), len(s), list(t), list(s), []

        def check(i):
            changed = False
            for j in range(m):
                if t[i + j] == '?': continue
                if t[i + j] != s[j]: return False
                changed = True
            if changed:
                t[i:i + m] = ['?'] * m
                res.append(i)
            return changed

        changed = True
        while changed:
            changed = False
            for i in range(n - m + 1):
                changed |= check(i)
        return res[::-1] if t == ['?'] * n else []