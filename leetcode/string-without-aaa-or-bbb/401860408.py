# title: string-without-aaa-or-bbb
# detail: https://leetcode.com/submissions/detail/401860408/
# datetime: Tue Sep 29 00:15:48 2020
# runtime: 28 ms
# memory: 14.2 MB

class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        a, b = 'a', 'b'
        if B > A:
            A, B = B, A
            a, b = b, a
        result = ''
        while A and B:
            if A > B:
                result += a * 2 + b
                A -= 2
            else:
                result += a + b
                A -= 1
            B -= 1
        if A:
            result += a * A
        return result