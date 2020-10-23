# title: maximum-nesting-depth-of-the-parentheses
# detail: https://leetcode.com/submissions/detail/409879561/
# datetime: Sun Oct 18 00:47:38 2020
# runtime: 40 ms
# memory: 14.1 MB

class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        max_depth = 0
        for c in s:
            if c == '(':
                depth += 1
            elif c == ')':
                depth -= 1
            max_depth = max(max_depth, depth)
        return max_depth