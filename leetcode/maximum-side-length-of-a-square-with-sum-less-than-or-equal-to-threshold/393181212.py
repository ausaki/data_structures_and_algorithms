# title: maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold
# detail: https://leetcode.com/submissions/detail/393181212/
# datetime: Wed Sep  9 15:23:01 2020
# runtime: 1808 ms
# memory: 18.6 MB

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m = len(mat)
        n = len(mat[0])
        for i in range(m):
            for j in range(n):
                mat[i][j] += (mat[i][j - 1] if j else 0) + (mat[i - 1][j] if i else 0) - (mat[i - 1][j - 1] if i and j else 0)
        k = 0
        for i in range(m):
            for j in range(n):
                l = k + 1
                r = min(m - i, n - j)
                if r < l:
                    break
                while l <= r:
                    mid = (l + r) // 2
                    s = mat[i + mid - 1][j + mid - 1] - (mat[i + mid - 1][j - 1] if j else 0) - (mat[i - 1][j + mid - 1] if i else 0) + (mat[i - 1][j - 1] if i and j else 0)
                    if s <= threshold:
                        l = mid + 1
                    else:
                        r = mid - 1
                k = max(k ,r)
        return k