# title: maximum-nesting-depth-of-two-valid-parentheses-strings
# detail: https://leetcode.com/submissions/detail/397370388/
# datetime: Fri Sep 18 14:55:06 2020
# runtime: 48 ms
# memory: 14.5 MB

class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        L = '('
        n = len(seq)
        result = [0] * n
        depth = 0
        for i, c in enumerate(seq):
            depth += c == L
            result[i] = depth % 2
            depth -= c != L
        return result