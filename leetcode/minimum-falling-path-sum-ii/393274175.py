# title: minimum-falling-path-sum-ii
# detail: https://leetcode.com/submissions/detail/393274175/
# datetime: Wed Sep  9 21:28:52 2020
# runtime: 288 ms
# memory: 17.3 MB

class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        n = len(arr)
        if n == 1:
            return arr[0][0]
        a, b = 0, 1
        if arr[0][a] > arr[0][b]:
            a, b = b, a
        for i in range(2, n):
            if arr[0][i] < arr[0][a]:
                a, b = i, a
            elif arr[0][i] < arr[0][b]:
                b = i
        for i in range(1, n):
            c, d = -1, -1
            for j in range(n):
                if j != a:
                    arr[i][j] += arr[i - 1][a]
                else:
                    arr[i][j] += arr[i - 1][b]
                if j == 0:
                    c = 0
                elif j == 1:
                    d = 1
                    if arr[i][c] > arr[i][d]:
                        c, d = d, c
                else:
                    if arr[i][j] < arr[i][c]:
                        c, d = j, c
                    elif arr[i][j] < arr[i][d]:
                        d = j
            a, b = c, d
        return arr[n - 1][a]                    
