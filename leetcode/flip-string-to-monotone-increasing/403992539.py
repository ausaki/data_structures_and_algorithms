# title: flip-string-to-monotone-increasing
# detail: https://leetcode.com/submissions/detail/403992539/
# datetime: Sun Oct  4 01:05:15 2020
# runtime: 56 ms
# memory: 14.9 MB

class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        g = [(k, len(list(l))) for k, l in itertools.groupby(S)]
        n = len(g)
        m = len(S)
        i = 0
        if g[i][0] == '0':
            i += 1
        ones = 0
        zeros = [0]
        for i in range(n):
            zeros.append((g[i][1] if g[i][0] == '0' else 0) + zeros[-1])
        i = 0
        if g[i][0] == '0':
            i += 1
        while i < n:
            if g[i][0] == '0':
                continue
            l = g[i][1]
            m = min(m, ones + zeros[-1] - zeros[i])
            ones += l
            i += 2
        return min(m, ones)
        