# title: champagne-tower
# detail: https://leetcode.com/submissions/detail/411806221/
# datetime: Thu Oct 22 16:12:18 2020
# runtime: 72 ms
# memory: 14.1 MB

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        q = [poured]
        for row in range(query_row):
            q2 = [0] * (len(q) + 1)
            for i, j in enumerate(q):
                if j <= 1:
                    continue
                overflow = j - 1
                q2[i] += overflow * 0.5
                q2[i + 1] += overflow * 0.5
            q = q2
        return min(q[query_glass], 1)
