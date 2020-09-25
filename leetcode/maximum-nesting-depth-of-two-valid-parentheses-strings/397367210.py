# title: maximum-nesting-depth-of-two-valid-parentheses-strings
# detail: https://leetcode.com/submissions/detail/397367210/
# datetime: Fri Sep 18 14:45:58 2020
# runtime: 52 ms
# memory: 14.2 MB

class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        L, R = '(', ')'
        stack = []
        n = len(seq)
        result = [0] * n
        depth = 0
        k = 0
        for i, c in enumerate(seq):
            if c == L:
                stack.append(i)
                result[i] = len(stack)
                depth = max(depth, len(stack))
            else:
                result[i] = len(stack)
                stack.pop()
            if not stack:
                for j in range(k, i + 1):
                    if result[j] <= depth // 2:
                        result[j] = 0
                    else:
                        result[j] = 1
                depth = 0
                k = i + 1
        return result