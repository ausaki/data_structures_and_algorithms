# title: find-longest-awesome-substring
# detail: https://leetcode.com/submissions/detail/379779031/
# datetime: Wed Aug 12 15:57:31 2020
# runtime: 1648 ms
# memory: 14.8 MB

class Solution:
    shifts = [(1 << i) for i in range(10)]
    
    def longestAwesome(self, s: str) -> int:
        n = len(s)
        prefix_sum = {0: -1}
        curr = 0
        result = 1
        for i, ch in enumerate(s):
            curr ^= self.shifts[ord(ch) - 48]
            for j in range(10):
                k = curr ^ self.shifts[j]
                result = max(result, i - prefix_sum.get(k, n))
            if curr not in prefix_sum:
                prefix_sum[curr] = i
            else:
                result = max(result, i - prefix_sum[curr])
        return result