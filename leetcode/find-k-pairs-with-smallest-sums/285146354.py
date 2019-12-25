# title: find-k-pairs-with-smallest-sums
# detail: https://leetcode.com/submissions/detail/285146354/
# datetime: Wed Dec 11 10:21:30 2019
# runtime: 52 ms
# memory: 13.1 MB

import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        def gen(u):
            for v in nums2:
                yield (u + v, [u, v])
                
        if (not nums1) or (not nums2):
            return []
        it = heapq.merge(*[gen(u) for u in nums1])
        res = [next(it)[1] for i in range(min(k, len(nums1) * len(nums2)))]
        return res