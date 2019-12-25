# title: longest-string-chain
# detail: https://leetcode.com/submissions/detail/278150598/
# datetime: Tue Nov 12 16:10:06 2019
# runtime: 152 ms
# memory: 13 MB

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        words = sorted(words, key=len)
        result = 0
        for w in words:
            dp[w] = max(dp.get(w[:i] + w[i + 1:], 0) for i in range(len(w))) + 1
            if dp[w] > result:
                result = dp[w]
        return result
        