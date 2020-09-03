# title: minimum-swaps-to-arrange-a-binary-grid
# detail: https://leetcode.com/submissions/detail/376039256/
# datetime: Wed Aug  5 01:15:07 2020
# runtime: 584 ms
# memory: 14.3 MB

class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        r0 = [0] * n
        for i in range(n):
            for j in reversed(range(n)):
                if grid[i][j] == 0:
                    r0[i] += 1
                else:
                    break
        r0_copy = sorted(r0, reverse=True)
        for i, j in enumerate(r0_copy):
            if i + j + 1 < n:
                return -1
        result = 0
        for i in range(n):
            for j in range(i, n):
                if r0[j] + i + 1 >= n:
                    t = r0[j]
                    for k in range(j - 1, i - 1, -1):
                        r0[k + 1] = r0[k]
                    r0[i] = t
                    result += j - i
                    break
        return result
        