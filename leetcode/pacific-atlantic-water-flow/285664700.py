# title: pacific-atlantic-water-flow
# detail: https://leetcode.com/submissions/detail/285664700/
# datetime: Fri Dec 13 16:28:28 2019
# runtime: 292 ms
# memory: 16.7 MB

from functools import lru_cache
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        M = len(matrix)
        if M == 0:
            return []
        N = len(matrix[0])
        
        def find(i, j, result):
            for ii, jj in [[i, j -1], [i, j + 1], [i - 1, j], [i + 1, j]]:
                if 0 <= ii < M and 0 <= jj < N and matrix[ii][jj] >= matrix[i][j] and ii * N + jj not in result:
                    result.add(ii * N + jj)
                    find(ii, jj, result)
        pacific = set()
        atlantic = set()
        for i in range(M):
            pacific.add(i * N + 0)
            find(i, 0, pacific)
            atlantic.add(i * N + N - 1)
            find(i, N - 1, atlantic)
        for j in range(N):
            pacific.add(j)
            find(0, j, pacific)
            atlantic.add((M - 1) * N + j)
            find(M - 1, j, atlantic)
        result = list(pacific & atlantic)
        result.sort()
        for i, j in enumerate(result):
            result[i] = [j // N, j % N]
        return result