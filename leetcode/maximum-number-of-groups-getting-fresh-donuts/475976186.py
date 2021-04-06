# title: maximum-number-of-groups-getting-fresh-donuts
# detail: https://leetcode.com/submissions/detail/475976186/
# datetime: Sun Apr  4 00:44:55 2021
# runtime: 1484 ms
# memory: 48.9 MB

class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        '''
        总结:
        我当时是想到使用 DP 的, 但是又觉得应该有其它贪心算法或者数学上的解法.
        '''
        rem = [0] * batchSize
        n = len(groups)
        res = 0
        for g in groups:
            r = g % batchSize 
            if r == 0:
                res += 1
            else:
                rem[r] += 1
        
        @lru_cache(None)
        def dp(rem, r):
            res = 0
            for i in range(1, batchSize):
                if rem[i] <= 0:
                    continue
                rem1 = rem[:i] + (rem[i] - 1,) + rem[i + 1:]
                res = max(res, dp(rem1, (r + i) % batchSize))
            if r == 0: res += 1
            if res == 0 and sum(rem) == 0:
                res += 1
            return res
        
        return res + dp(tuple(rem), 0) - 1