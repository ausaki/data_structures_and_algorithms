# title: remove-palindromic-subsequences
# detail: https://leetcode.com/submissions/detail/390846624/
# datetime: Fri Sep  4 15:40:30 2020
# runtime: 24 ms
# memory: 13.9 MB

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        i = 0
        j = n - 1
        while i <= j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return 2
        return 1
