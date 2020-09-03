# title: regular-expression-matching
# detail: https://leetcode.com/submissions/detail/343383022/
# datetime: Sat May 23 14:33:56 2020
# runtime: 60 ms
# memory: 13.7 MB

import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return bool(re.fullmatch(p, s))