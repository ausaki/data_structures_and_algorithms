# title: masking-personal-information
# detail: https://leetcode.com/submissions/detail/408960920/
# datetime: Thu Oct 15 14:44:30 2020
# runtime: 24 ms
# memory: 14.1 MB

class Solution:
    def maskPII(self, S: str) -> str:
        at = S.find('@')
        if at >= 0:
            return (S[0] + '*' * 5 + S[at - 1:]).lower()
        digits = [c for c in S if c.isdigit()]
        if len(digits) == 10:
            return '***-***-{}'.format(''.join(digits[-4:]))
        return '+{}-***-***-{}'.format('*' * (len(digits) - 10), ''.join(digits[-4:]))
            