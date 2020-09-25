# title: longest-chunked-palindrome-decomposition
# detail: https://leetcode.com/submissions/detail/396958232/
# datetime: Thu Sep 17 16:15:36 2020
# runtime: 40 ms
# memory: 13.8 MB

class Solution:
    def longestDecomposition(self, text: str) -> int:
        n = len(text)
        i, j = 0, n - 1
        result = 0
        while i <= j:
            for k in range(1, (j - i + 1) // 2 + 1):
                if text[i:i + k] == text[j - k + 1:j + 1]:
                    result += 2
                    i, j  = i + k, j - k
                    break
            else:
                result += 1
                break
        return result