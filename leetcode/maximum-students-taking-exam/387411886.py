# title: maximum-students-taking-exam
# detail: https://leetcode.com/submissions/detail/387411886/
# datetime: Fri Aug 28 12:06:58 2020
# runtime: 108 ms
# memory: 22.3 MB

class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m = len(seats)
        n = len(seats[0])
        @lru_cache(None)
        def dp(i, j, curr, row):
            if j == n:
                return dp(i + 1, 0, 0, curr)
            if i == m:
                return 0
            if seats[i][j] == '#':
                return dp(i, j + 1, curr, row)
            l = curr & (1 << (j - 1)) if j > 0 else 0
            ul = row & (1 << (j - 1)) if j > 0 else 0
            ur = row & (1 << (j + 1)) if j < n - 1 else 0
            a = dp(i, j + 1, curr, row)
            b = 0
            if l + ul + ur == 0:
                b = 1 + dp(i, j + 1, curr | (1 << j), row)
            return max(a, b)
        
        return dp(0, 0, 0, 0)