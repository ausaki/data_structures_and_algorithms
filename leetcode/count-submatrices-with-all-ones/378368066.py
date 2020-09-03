# title: count-submatrices-with-all-ones
# detail: https://leetcode.com/submissions/detail/378368066/
# datetime: Sun Aug  9 19:57:50 2020
# runtime: 264 ms
# memory: 13.9 MB

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        M, N = len(mat), len(mat[0])
        for i in range(1, M):
            for j in range(N):
                if mat[i][j] == 1:
                    mat[i][j] += mat[i - 1][j]
        result = 0
        for i in range(M):
            stack = []
            cnt = 0
            for j in range(N):
                while stack and mat[i][stack[-1]] > mat[i][j]:
                    r = stack.pop()
                    l = stack[-1] if stack else -1
                    cnt -= (mat[i][r] - mat[i][j]) * (r - l)
                stack.append(j)
                cnt += mat[i][j]
                result += cnt
        return result
