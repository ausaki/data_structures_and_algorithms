# title: maximum-number-of-events-that-can-be-attended-ii
# detail: https://leetcode.com/submissions/detail/452792044/
# datetime: Sun Feb  7 00:20:19 2021
# runtime: 908 ms
# memory: 219.3 MB

'''
我大概在半个小时左右就应该可以完成比赛了, 但是我花了不少时间在思考是否有比 `dp(i, j, k)` 更好的算法. 一直没有想到更好的算法, 于是我就提交了 `dp(i, j, k)` 的解法, 没想到没有超时.


提交成功后, 我又尝试了二维数组的 dp 解法, 不过超时了. 复杂度比递归版本的 dp 更高, 但是相对来说内存占用少.

一个小优化, 将 events 按照 endDay 分组, 同一组的 events 再按照 `(val, startDay)` 排序. 最后再使用递归版本的 dp 求解. 这个优化应该可以提升一些性能.
'''

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        @lru_cache(None)
        def dp(i, k):
            if i == n or k == 0:
                return 0
            e = events[i][1] + 1
            j = bisect.bisect(events, [e], i)
            return max(events[i][2] + dp(j, k - 1), dp(i + 1, k))
        
        n = len(events)
        events.sort()
        return dp(0, k)
    
        # events.sort(key=lambda e: (e[1], s[0], -e[2]))
        # dp = [[0] * (k + 1) for i in range(n + 1)]
        # for i in range(n - 1, -1, -1):
        #     for j in range(-1, i):
        #         for k_ in range(1, k + 1):
        #             if j < 0 or events[i][0] > events[j][1]:
        #                 dp[j][k_] = max(events[i][2] + dp[i][k_ - 1], dp[j][k_])
        # return dp[-1][k]
        