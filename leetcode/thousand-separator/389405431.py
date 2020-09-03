# title: thousand-separator
# detail: https://leetcode.com/submissions/detail/389405431/
# datetime: Tue Sep  1 20:15:28 2020
# runtime: 36 ms
# memory: 13.7 MB

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
                result.append(('0' if m >= 10 else '00') + str(m))
        return '.'.join(reversed(result))