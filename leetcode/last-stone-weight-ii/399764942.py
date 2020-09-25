# title: last-stone-weight-ii
# detail: https://leetcode.com/submissions/detail/399764942/
# datetime: Thu Sep 24 02:12:09 2020
# runtime: 36 ms
# memory: 13.9 MB

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        M = 10 ** 9
        sums = {0}
        for s in stones:
            new = set()
            for s0 in sums:
                new.add(s0 + s)
                new.add(s0 - s)
            sums = new
        m = 10 ** 9
        for s in sums:
            if s >= 0:
                m = min(m, s)
        return m