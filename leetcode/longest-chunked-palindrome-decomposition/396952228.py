# title: longest-chunked-palindrome-decomposition
# detail: https://leetcode.com/submissions/detail/396952228/
# datetime: Thu Sep 17 15:54:54 2020
# runtime: 56 ms
# memory: 13.9 MB

class Solution:
    def longestDecomposition(self, text: str) -> int:
        n = len(text)
        @lru_cache(None)
        def dp(i):
            j = n - i - 1
            if i == j:
                return 1
            if i > j:
                return 0
            result = -1
            for k in range(1, (j - i + 1) // 2 + 1):
                if text[i:i + k] == text[j - k + 1:j + 1]:
                    result = max(result, dp(i + k))
            return (result + 2) if result != -1 else 1
        
        return dp(0)