# title: reformat-the-string
# detail: https://leetcode.com/submissions/detail/383275076/
# datetime: Thu Aug 20 00:22:20 2020
# runtime: 48 ms
# memory: 13.9 MB

class Solution:
    def reformat(self, s: str) -> str:
        letters = []
        digits = []
        for c in s:
            if c.isdigit():
                digits.append(c)
            else:
                letters.append(c)
        n = len(letters)
        m = len(digits)
        if abs(n - m) > 1:
            return ''
        result = ''
        i = 0
        j = 0
        if n < m:
            letters, digits = digits, letters
            n, m = m, n
        while i < m:
            result += letters[i] + digits[i]
            i += 1
        if i < n:
            result += letters[i]
        return result