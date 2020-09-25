# title: letter-tile-possibilities
# detail: https://leetcode.com/submissions/detail/397844450/
# datetime: Sat Sep 19 21:35:21 2020
# runtime: 60 ms
# memory: 13.8 MB

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        cnt = list(collections.Counter(tiles).values())
        n = len(cnt)
        c = [0] * n
        def make(i):
            if i == n:
                s = 1
                for j in c:
                    s *= math.factorial(j)
                return math.factorial(sum(c)) // s
            s = 0
            for j in range(cnt[i] + 1):
                c[i] = j
                s += make(i + 1)
            return s
        return make(0) - 1
