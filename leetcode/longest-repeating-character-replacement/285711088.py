# title: longest-repeating-character-replacement
# detail: https://leetcode.com/submissions/detail/285711088/
# datetime: Fri Dec 13 23:59:16 2019
# runtime: 172 ms
# memory: 14 MB

from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        N = len(s)
        min_len = min(k, N)
        dp = defaultdict(list)
        prev = 'x'
        i = 0
        while i < N:
            j = i
            while j + 1 < N and s[j] == s[j + 1]:
                j += 1
            dp[s[i]].append([i, j])
            i = j + 1
        res = 0
        print(dp)
        for char, ranges in dp.items():
            M = len(ranges)
            start = 0
            while start < M:
                end = start
                m = k
                while start <= end and end + 1 < M:
                    gap = ranges[end + 1][0] - ranges[end][1] - 1
                    if gap <= m:
                        end += 1
                        m -= gap
                    else:
                        res = max(res, ranges[end][1] - ranges[start][0] + 1 + m)
                        m += ranges[start + 1][0] - ranges[start][1] - 1
                        start += 1
                if start <= end:
                    r = ranges[end][1] - ranges[start][0] + 1
                    res = max(res, r + min(m, ranges[start][0] + N - ranges[end][1] - 1))
                if end + 1 >= M:
                    break
        return res
                    
            
            
                