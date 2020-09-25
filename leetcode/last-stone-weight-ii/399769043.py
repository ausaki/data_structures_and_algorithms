# title: last-stone-weight-ii
# detail: https://leetcode.com/submissions/detail/399769043/
# datetime: Thu Sep 24 02:23:24 2020
# runtime: 44 ms
# memory: 13.7 MB

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
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