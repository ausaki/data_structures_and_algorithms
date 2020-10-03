# title: odd-even-jump
# detail: https://leetcode.com/submissions/detail/402243421/
# datetime: Tue Sep 29 20:57:45 2020
# runtime: 504 ms
# memory: 18.8 MB

class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        n = len(A)
        dp = [[0, 0] for i in range(n)]
        dp[n - 1] = [1, 1]
        B = [(A[-1], n - 1)]
        result = 1
        for i in range(n - 2, -1, -1):
            j = bisect.bisect(B, (A[i], i))
            if j < len(B):
                k = B[j][1]
                if dp[k][0]:
                    dp[i][1] = 1
                    result += 1
                if B[j][0] == A[i] and dp[k][1]:
                    dp[i][0] = 1
            if j > 0 and dp[i][0] == 0:
                k = bisect.bisect(B, (B[j - 1][0], 0))
                if dp[B[k][1]][1]:
                    dp[i][0] = 1
            B.insert(j, (A[i], i))
        return result
            