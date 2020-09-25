# title: break-a-palindrome
# detail: https://leetcode.com/submissions/detail/390964178/
# datetime: Fri Sep  4 23:46:54 2020
# runtime: 24 ms
# memory: 13.8 MB

class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1:
            return ''
        m = n // 2
        for i in range(m):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i + 1:]
        return palindrome[:-1] + 'b'