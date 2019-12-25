# title: kth-smallest-element-in-a-sorted-matrix
# detail: https://leetcode.com/submissions/detail/285227658/
# datetime: Wed Dec 11 17:03:29 2019
# runtime: 212 ms
# memory: 18.6 MB

import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        seq = heapq.merge(*matrix)
        res = 0
        for i in range(k):
            res = next(seq)
        return res