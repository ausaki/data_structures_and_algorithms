# title: thousand-separator
# detail: https://leetcode.com/submissions/detail/389388094/
# datetime: Tue Sep  1 19:03:44 2020
# runtime: 32 ms
# memory: 13.9 MB

class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n == 0:
            return '0'
        result = []
        while n:
            n, m = divmod(n, 1000)
            if n == 0 or m >= 100:
                result.append(str(m))
            else:
                result.append('0' + str(m))
        return '.'.join(reversed(result))