# title: find-k-pairs-with-smallest-sums
# detail: https://leetcode.com/submissions/detail/285147270/
# datetime: Wed Dec 11 10:26:33 2019
# runtime: 192 ms
# memory: 13.1 MB

import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = heapq.nsmallest(k, ((u + v, [u, v]) for u in nums1 for v in nums2))
        return [item[1] for item in res]