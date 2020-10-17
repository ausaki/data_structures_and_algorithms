# title: ambiguous-coordinates
# detail: https://leetcode.com/submissions/detail/409323668/
# datetime: Fri Oct 16 12:51:12 2020
# runtime: 48 ms
# memory: 14.2 MB

class Solution:
    def ambiguousCoordinates(self, S: str) -> List[str]:
        def make(s):
            n = len(s)
            if s[0] == '0':
                if s[-1] != '0' or n == 1:
                    yield '0' + (('.' + s[1:]) if n > 1 else '')
                return 
            if s[-1] == '0':
                yield s
                return
            for i in range(1, n):
                yield s[:i] + '.' + s[i:]
            yield s
        result = []
        S = S[1:-1]
        for i in range(1, len(S)):
            result.extend('({}, {})'.format(x, y) for x, y in itertools.product(make(S[:i]), make(S[i:])))
        return result
            