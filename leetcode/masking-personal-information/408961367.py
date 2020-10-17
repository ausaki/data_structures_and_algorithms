# title: masking-personal-information
# detail: https://leetcode.com/submissions/detail/408961367/
# datetime: Thu Oct 15 14:45:54 2020
# runtime: 28 ms
# memory: 13.9 MB

class Solution:
    def maskPII(self, S: str) -> str:
        at = S.find('@')
        if at >= 0:
            return '{}*****{}'.format(S[0], S[at - 1:]).lower()
        digits = [c for c in S if c.isdigit()]
        if len(digits) == 10:
            return '***-***-{}'.format(''.join(digits[-4:]))
        return '+{}-***-***-{}'.format('*' * (len(digits) - 10), ''.join(digits[-4:]))
            