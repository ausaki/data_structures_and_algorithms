# title: kth-smallest-element-in-a-sorted-matrix
# detail: https://leetcode.com/submissions/detail/285235525/
# datetime: Wed Dec 11 18:10:56 2019
# runtime: 220 ms
# memory: 18.6 MB

import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        N = len(matrix)
        def gen(i):
            for j in range(N):
                yield matrix[i][j]
                
        seq = heapq.merge(*[gen(i) for i in range(N)])
        res = 0
        for i in range(k):
            res = next(seq)
        return res