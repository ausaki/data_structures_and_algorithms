# title: champagne-tower
# detail: https://leetcode.com/submissions/detail/411803837/
# datetime: Thu Oct 22 16:03:44 2020
# runtime: 76 ms
# memory: 14.1 MB

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        q = [poured]
        row = 0
        while q and row < query_row:
            if row == query_row:
                return q[query_glass]
            q2 = [0] * (len(q) + 1)
            for i, j in enumerate(q):
                if j <= 1:
                    continue
                overflow = j - 1
                q2[i] += overflow * 0.5
                q2[i + 1] += overflow * 0.5
            q = q2
            row += 1
        return min(q[query_glass], 1) if row == query_row else 0
