# title: can-you-eat-your-favorite-candy-on-your-favorite-day?
# detail: https://leetcode.com/submissions/detail/449954157/
# datetime: Sun Jan 31 11:25:08 2021
# runtime: 3404 ms
# memory: 72.9 MB

class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        prefix = [0]
        for i in candiesCount:
            prefix.append(prefix[-1] + i)
        res = []
        for t, d, c in queries:
            low = (d + 1)
            high = (d + 1) * c
            i = bisect.bisect(prefix, low)
            j = bisect.bisect(prefix, high)
            if high == prefix[j - 1]:
                j -= 1
            if low == prefix[i - 1]:
                i -= 1
            i -= 1
            j -= 1
            res.append(i <= t <= j)
        return res
                