# title: letter-tile-possibilities
# detail: https://leetcode.com/submissions/detail/397845200/
# datetime: Sat Sep 19 21:38:28 2020
# runtime: 36 ms
# memory: 13.7 MB

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        cnt = list(collections.Counter(tiles).values())
        n = len(cnt)
        def make(i):
            if i == n:
                s = 1
                for j in cnt:
                    s *= math.factorial(j)
                return math.factorial(sum(cnt)) // s
            s = 0
            for j in range(cnt[i] + 1):
                cnt[i] = j
                s += make(i + 1)
            return s
        return make(0) - 1
