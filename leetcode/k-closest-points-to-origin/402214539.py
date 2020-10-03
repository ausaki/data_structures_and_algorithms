# title: k-closest-points-to-origin
# detail: https://leetcode.com/submissions/detail/402214539/
# datetime: Tue Sep 29 18:46:27 2020
# runtime: 660 ms
# memory: 19.6 MB

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        return heapq.nsmallest(K, points, key=lambda p: p[0] ** 2 + p[1] ** 2)