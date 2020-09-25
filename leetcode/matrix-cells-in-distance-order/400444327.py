# title: matrix-cells-in-distance-order
# detail: https://leetcode.com/submissions/detail/400444327/
# datetime: Fri Sep 25 14:04:19 2020
# runtime: 164 ms
# memory: 15.7 MB

class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        return sorted([[i, j] for i in range(R) for j in range(C)], key=lambda pos: abs(r0 - pos[0]) + abs(c0- pos[1]))