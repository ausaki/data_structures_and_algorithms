# title: koko-eating-bananas
# detail: https://leetcode.com/submissions/detail/406579570/
# datetime: Fri Oct  9 22:47:55 2020
# runtime: 444 ms
# memory: 15.2 MB

class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        n = len(piles)
        if H == n:
            return max(piles)
        piles.sort()
        l, r = 1, piles[-1]
        while l <= r:
            m = (l + r) // 2
            i = bisect.bisect(piles, m)
            h = i
            for j in range(i, n):
                h += (piles[j] + m - 1) // m
            if h > H:
                l = m + 1
            else:
                r = m - 1
        return l
        