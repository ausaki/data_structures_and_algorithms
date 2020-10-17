# title: shortest-distance-to-a-character
# detail: https://leetcode.com/submissions/detail/409074754/
# datetime: Thu Oct 15 22:48:37 2020
# runtime: 36 ms
# memory: 14.1 MB

class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        n = len(S)
        res = []
        l, r = -1, -1
        for i, c in enumerate(S):
            if c == C:
                res.append(0)
                l = i
            else:
                while r <= i or (r < n and S[r] != C):
                    r += 1
                res.append(min(r - i if r < n else n, i - l if l >= 0 else n))
        return res
                    