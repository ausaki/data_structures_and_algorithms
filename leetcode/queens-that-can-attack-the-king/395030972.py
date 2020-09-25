# title: queens-that-can-attack-the-king
# detail: https://leetcode.com/submissions/detail/395030972/
# datetime: Sun Sep 13 17:42:00 2020
# runtime: 36 ms
# memory: 13.8 MB

class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        n = 8
        result = []
        for di, dj in itertools.product(range(-1, 2), range(-1, 2)):
            if di == 0 and dj == 0:
                continue
            i, j = king
            while 0 <= i < n and 0 <= j < n and [i, j] not in queens:
                i += di
                j += dj
            if 0 <= i < n and 0 <= j < n:
                result.append([i, j])
        return result
                