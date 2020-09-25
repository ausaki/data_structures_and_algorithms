# title: maximum-nesting-depth-of-two-valid-parentheses-strings
# detail: https://leetcode.com/submissions/detail/397368810/
# datetime: Fri Sep 18 14:50:37 2020
# runtime: 44 ms
# memory: 14.3 MB

class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        L = '('
        stack = []
        n = len(seq)
        result = [0] * n
        for i, c in enumerate(seq):
            if c == L:
                stack.append(i)
                if len(stack) % 2:
                    result[i] = 1
            else:
                if len(stack) % 2:
                    result[i] = 1
                stack.pop()
        return result