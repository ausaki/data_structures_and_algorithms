# title: number-of-submatrices-that-sum-to-target
# detail: https://leetcode.com/submissions/detail/399599402/
# datetime: Wed Sep 23 16:22:44 2020
# runtime: 1028 ms
# memory: 14.7 MB

class Solution:
    def numSubmatrixSumTarget(self, A, target):
        xrange = range
        m, n = len(A), len(A[0])
        for row in A:
            for i in xrange(n - 1):
                row[i + 1] += row[i]
        res = 0
        for i in xrange(n):
            for j in xrange(i, n):
                c = collections.defaultdict(int)
                cur, c[0] = 0, 1
                for k in xrange(m):
                    cur += A[k][j] - (A[k][i - 1] if i > 0 else 0)
                    res += c[cur - target]
                    c[cur] += 1
        return res
                    