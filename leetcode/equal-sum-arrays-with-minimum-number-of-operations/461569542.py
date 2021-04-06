# title: equal-sum-arrays-with-minimum-number-of-operations
# detail: https://leetcode.com/submissions/detail/461569542/
# datetime: Sun Feb 28 13:00:06 2021
# runtime: 1304 ms
# memory: 18.4 MB

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        s1, s2 = sum(nums1), sum(nums2)
        if s1 == s2: return 0
        if n > 6 * m or m > 6 * n: return -1
            
        g1, g2 = collections.Counter(nums1), collections.Counter(nums2)
        if s1 > s2:
            s1, s2 = s2, s1
            g1, g2 = g2, g1
            n, m = m, n
        diff = abs(s1 - s2)
        q = []
        for i, j in g1.items():
            if i != 6:
                heapq.heappush(q, (i - 6, -j))
        for i, j in g2.items():
            if i != 1:
                heapq.heappush(q, (1 - i, -j))
        res = 0
        while diff > 0:
            i, j = heapq.heappop(q)
            i, j = -i, -j
            t, r = divmod(diff, i)
            t += r != 0
            res += min(t, j)
            diff -= min(t, j) * i
        return res
            