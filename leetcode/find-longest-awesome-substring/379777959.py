# title: find-longest-awesome-substring
# detail: https://leetcode.com/submissions/detail/379777959/
# datetime: Wed Aug 12 15:54:16 2020
# runtime: 1688 ms
# memory: 14.7 MB

class Solution:
    def longestAwesome(self, s: str) -> int:
        n = len(s)
        prefix_sum = {0: -1}
        curr = 0
        result = 1
        for i, ch in enumerate(s):
            d = int(ch)
            curr ^= 1 << d
            for j in range(10):
                k = curr ^ (1 << j)
                result = max(result, i - prefix_sum.get(k, n))
            if curr not in prefix_sum:
                prefix_sum[curr] = i
            else:
                result = max(result, i - prefix_sum[curr])
        return result