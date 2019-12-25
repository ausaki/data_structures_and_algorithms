# title: nth-digit
# detail: https://leetcode.com/submissions/detail/282289010/
# datetime: Thu Nov 28 23:40:38 2019
# runtime: 28 ms
# memory: 12.7 MB

class Solution:
    def findNthDigit(self, n: int) -> int:
        i = 1
        j = 9
        while n > j:
            n -= j
            i += 1
            j = i * (10 ** i - 10 ** (i - 1))
        k, m = divmod(n, i)
        a = 10 ** (i - 1) + k - 1
        b = a + 1
        if m == 0:
            return a % 10
        else:
            return int(str(b)[m - 1])