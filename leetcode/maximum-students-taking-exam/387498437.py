# title: maximum-students-taking-exam
# detail: https://leetcode.com/submissions/detail/387498437/
# datetime: Fri Aug 28 16:10:18 2020
# runtime: 64 ms
# memory: 13.8 MB

class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m = len(seats)
        n = len(seats[0])
        # @lru_cache(None)
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
        
        # return dp(0, 0, 0, 0)
        def bitcount(x):
            cnt = 0
            while x:
                cnt += 1
                x &= x - 1
            return cnt
        
        rows = {0: 0}
        for i in range(m):
            new_rows = {}
            for row in rows:
                dp = [[0], []]
                for j in range(n):
                    l = len(dp[0])
                    dp[0].extend(dp[1])
                    dp[1].clear()
                    if seats[i][j] == '#':
                        continue
                    ul = row & (1 << (j - 1)) if j > 0 else 0
                    ur = row & (1 << (j + 1)) if j < n - 1 else 0
                    if ul + ur == 0:
                        for k in range(l):
                            dp[1].append(dp[0][k] | (1 << j))
                # print(dp)
                for k in dp[0]:
                    new_rows[k] = max(new_rows.get(k, 0), rows[row] + bitcount(k))
                for k in dp[1]:
                    new_rows[k] = max(new_rows.get(k, 0), rows[row] + bitcount(k))
            rows = new_rows
        return max(rows.values())