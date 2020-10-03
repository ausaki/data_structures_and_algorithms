# title: grid-illumination
# detail: https://leetcode.com/submissions/detail/401448954/
# datetime: Mon Sep 28 01:10:38 2020
# runtime: 900 ms
# memory: 30.2 MB

class Solution:
    def gridIllumination(self, N: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        rows = collections.Counter()
        cols = collections.Counter()
        dia1 = collections.Counter()
        dia2 = collections.Counter()
        lamps_set = set()
        for i, j in lamps:
            rows[i] += 1
            cols[j] += 1
            dia1[i - j] += 1
            dia2[i + j] += 1
            lamps_set.add((i, j))
        result = []
        for i, j in queries:
            if i in rows or j in cols or i - j in dia1 or i + j in dia2:
                result.append(1)
            else:
                result.append(0)
                continue
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    ii, jj = i + di, j + dj
                    if 0 <= ii < N and 0 <= jj < N and (ii, jj) in lamps_set:
                        lamps_set.remove((ii, jj))
                        rows[ii] -= 1
                        if rows[ii] == 0:
                            rows.pop(ii)
                        cols[jj] -= 1
                        if cols[jj] == 0:
                            cols.pop(jj)
                        dia1[ii - jj] -= 1
                        if dia1[ii - jj] == 0:
                            dia1.pop(ii - jj)
                        dia2[ii + jj] -= 1
                        if dia2[ii + jj] == 0:
                            dia2.pop(ii + jj)
        return result    
                            