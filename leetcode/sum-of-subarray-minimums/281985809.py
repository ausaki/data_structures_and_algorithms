# title: sum-of-subarray-minimums
# detail: https://leetcode.com/submissions/detail/281985809/
# datetime: Wed Nov 27 13:11:17 2019
# runtime: 524 ms
# memory: 16.8 MB

import bisect
class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        dp = []
        res = 0
        prev = 0
        for n in A:
            # print(dp)
            cur = prev
            item = [n, 1]
            j = len(dp) - 1
            while j >= 0 and dp[j][0] > n:
                cur -= (dp[j][0] - n) * dp[j][1]
                item[1] += dp[j][1]
                dp.pop()
                j -= 1
                
            dp.append(item)
            cur += n
            prev = cur
            res = (res + cur) % (10 ** 9 + 7)
        return res