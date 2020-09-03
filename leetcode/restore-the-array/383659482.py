# title: restore-the-array
# detail: https://leetcode.com/submissions/detail/383659482/
# datetime: Thu Aug 20 18:12:12 2020
# runtime: 1048 ms
# memory: 14.6 MB

class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        n = len(s)
        b = ord('0')
        MOD = 10 ** 9 + 7
        dp = collections.deque([0] * 10)
        dp[0] = 1
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                dp.pop()
                dp.appendleft(0)
                continue
            num = 0
            cnt = 0
            for j in range(i, n):
                num = num * 10 + ord(s[j]) - b
                if num <= k:
                    cnt += dp[j - i] % MOD
                else:
                    break
            dp.appendleft(cnt % MOD)
            dp.pop()
        return dp[0]
                    
                
            