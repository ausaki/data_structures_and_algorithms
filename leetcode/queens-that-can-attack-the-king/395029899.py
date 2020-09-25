# title: queens-that-can-attack-the-king
# detail: https://leetcode.com/submissions/detail/395029899/
# datetime: Sun Sep 13 17:37:51 2020
# runtime: 44 ms
# memory: 13.9 MB

class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        n = 8
        result = []
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if di == 0 and dj == 0:
                    continue
                i, j = king
                while 0 <= i < n and 0 <= j < n and [i, j] not in queens:
                    i += di
                    j += dj
                if 0 <= i < n and 0 <= j < n:
                    result.append([i, j])
        return result
                