# title: kth-smallest-element-in-a-sorted-matrix
# detail: https://leetcode.com/submissions/detail/412204432/
# datetime: Fri Oct 23 16:54:25 2020
# runtime: 160 ms
# memory: 19.8 MB

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def count(val):
            cnt = 0
            j = n
            for i in range(n):
                j = bisect.bisect(matrix[i], val, 0, j)
                cnt += j
                if j == 0:
                    break
            return cnt
        
        n = len(matrix)
        l, r = matrix[0][0], matrix[n - 1][n - 1]
        while l <= r:
            m = l + (r - l) // 2 # (l + r) // 2
            cnt = count(m)
            if cnt < k:
                l = m + 1
            else:
                r = m - 1
        return l