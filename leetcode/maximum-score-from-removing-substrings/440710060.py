# title: maximum-score-from-removing-substrings
# detail: https://leetcode.com/submissions/detail/440710060/
# datetime: Sat Jan  9 23:15:32 2021
# runtime: 980 ms
# memory: 15.1 MB

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        g = []
        res = 0
        s += 'z'
        for c in s:
            if c not in 'ab':
                if len(g) > 1:
                    res += min(g[0][1], g[1][1]) * (x if g[0][0] == 'a' else y)
                g = []
                continue
            if g and c == g[-1][0]:
                g[-1][1] += 1
                continue
            if not g:
                g.append([c, 1])
                continue
            if g[-1][0] == 'a' and x > y:
                g[-1][1] -= 1
                res += x
            elif g[-1][0] == 'b' and y > x:
                g[-1][1] -= 1
                res += y
            else:
                g.append([c, 1])
            if g[-1][1] == 0:
                g.pop()
        return res
                    