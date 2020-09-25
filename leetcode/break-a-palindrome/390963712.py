# title: break-a-palindrome
# detail: https://leetcode.com/submissions/detail/390963712/
# datetime: Fri Sep  4 23:45:35 2020
# runtime: 28 ms
# memory: 13.7 MB

class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        m = n // 2
        for i in range(m):
            if palindrome[i] == 'a':
                continue
            return palindrome[:i] + 'a' + palindrome[i + 1:]
        return '' if n == 1 else palindrome[:-1] + 'b'