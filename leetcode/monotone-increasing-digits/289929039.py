# title: monotone-increasing-digits
# detail: https://leetcode.com/submissions/detail/289929039/
# datetime: Tue Dec 31 11:21:24 2019
# runtime: 28 ms
# memory: 12.7 MB

class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        if N < 10:
            return N
        digits = list(str(N))
        n = len(digits)
        i = 0
        while i + 1 < n and digits[i] <= digits[i + 1]:
            i += 1
        if i == n - 1:
            return N
        j = i - 1
        while j >= 0 and digits[j] == digits[i]:
            j -= 1
        j += 1
        digits[j] = chr(ord(digits[j]) - 1)
        j += 1
        while j < n:
            digits[j] = '9'
            j += 1
        return int(''.join(digits))
            