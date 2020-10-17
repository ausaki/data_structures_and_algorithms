# title: three-equal-parts
# detail: https://leetcode.com/submissions/detail/404238758/
# datetime: Sun Oct  4 12:46:48 2020
# runtime: 376 ms
# memory: 15 MB

class Solution:
    def threeEqualParts(self, A: List[int]) -> List[int]:
        n = len(A)
        ones = A.count(1)
        if ones % 3:
            return [-1, -1]
        if ones == 0:
            return [0, n - 1]
        t = ones // 3
        breaks = []
        ones = 0
        for i, j in enumerate(A):
            if j == 0:
                continue
            ones += 1
            if ones in [1, t + 1, 2 * t + 1]:
                breaks.append(i)
            if ones in [t, 2 * t, 3 * t]:
                breaks.append(i)
        i1, j1, i2, j2, i3, j3 = breaks
        if not (A[i1:j1 + 1] == A[i2: j2 + 1] == A[i3: j3 + 1]):
            return [-1, -1]
        x = i2 - j1 - 1
        y = i3 - j2 - 1
        z = n - j3 - 1
        if x >= z and y >= z:
            return [j1 + z, j2 + z + 1]
        return [-1, -1]
        
        