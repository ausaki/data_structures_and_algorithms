# title: longest-chunked-palindrome-decomposition
# detail: https://leetcode.com/submissions/detail/396957300/
# datetime: Thu Sep 17 16:12:18 2020
# runtime: 24 ms
# memory: 14 MB

class Solution:
    def longestDecomposition(self, text: str) -> int:
        n = len(text)
        def dp(i, j):
            if i == j:
                return 1
            if i > j:
                return 0
            for k in range(1, (j - i + 1) // 2 + 1):
                if text[i:i + k] == text[j - k + 1:j + 1]:
                    return 2 + dp(i + k, j - k)
            return 1
        
        return dp(0, n - 1)