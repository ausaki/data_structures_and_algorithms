# title: grid-illumination
# detail: https://leetcode.com/submissions/detail/401450177/
# datetime: Mon Sep 28 01:14:30 2020
# runtime: 932 ms
# memory: 30 MB

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
            if rows[i] or cols[j] or dia1[i - j] or dia2[i + j]:
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
                        cols[jj] -= 1
                        dia1[ii - jj] -= 1
                        dia2[ii + jj] -= 1
        return result    
                            