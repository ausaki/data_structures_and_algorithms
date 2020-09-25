# title: maximum-nesting-depth-of-two-valid-parentheses-strings
# detail: https://leetcode.com/submissions/detail/397369637/
# datetime: Fri Sep 18 14:52:55 2020
# runtime: 48 ms
# memory: 14.3 MB

class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        L = '('
        n = len(seq)
        result = [0] * n
        depth = 0
        for i, c in enumerate(seq):
            if c == L:
                depth += 1
                if depth % 2:
                    result[i] = 1
            else:
                if depth % 2:
                    result[i] = 1
                depth -= 1
        return result