# title: k-closest-points-to-origin
# detail: https://leetcode.com/submissions/detail/402214340/
# datetime: Tue Sep 29 18:45:35 2020
# runtime: 632 ms
# memory: 19.6 MB

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key=lambda p: p[0] ** 2 + p[1] ** 2)
        return points[:K]