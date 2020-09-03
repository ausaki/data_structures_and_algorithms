# title: the-k-weakest-rows-in-a-matrix
# detail: https://leetcode.com/submissions/detail/390466522/
# datetime: Thu Sep  3 21:30:08 2020
# runtime: 116 ms
# memory: 14 MB

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return [i for _, i in heapq.nsmallest(k, ((row.count(1), i) for i, row in enumerate(mat)))]