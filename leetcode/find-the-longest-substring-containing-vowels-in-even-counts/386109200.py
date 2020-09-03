# title: find-the-longest-substring-containing-vowels-in-even-counts
# detail: https://leetcode.com/submissions/detail/386109200/
# datetime: Tue Aug 25 18:16:22 2020
# runtime: 556 ms
# memory: 19.2 MB

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        m = {'a': 1, 'e': 1 << 1, 'i': 1 << 2, 'o': 1 << 3, 'u': 1 << 4}
        dp = {0: -1}
        prefix = 0
        l = 0
        result = 0
        for i, c in enumerate(s):
            if c not in m:
                l += 1
            else:
                prefix ^= m[c]
                if prefix not in dp:
                    dp[prefix] = i
                    l = 0
                else:
                    l = i - dp[prefix]
            result = max(result, l)
        return result