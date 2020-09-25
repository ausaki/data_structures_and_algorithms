# title: minimum-falling-path-sum-ii
# detail: https://leetcode.com/submissions/detail/393275392/
# datetime: Wed Sep  9 21:33:00 2020
# runtime: 276 ms
# memory: 17.2 MB

class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        n = len(arr)
        if n == 1:
            return arr[0][0]
        
        def min2(arr):
            a, b = 0, 1
            if arr[a] > arr[b]:
                a, b = b, a
            for i in range(2, n):
                if arr[i] < arr[a]:
                    a, b = i, a
                elif arr[i] < arr[b]:
                    b = i
            return a, b
        
        for i in range(1, n):
            a, b = min2(arr[i - 1])
            for j in range(n):
                if j != a:
                    arr[i][j] += arr[i - 1][a]
                else:
                    arr[i][j] += arr[i - 1][b]
        return min(arr[n - 1])
