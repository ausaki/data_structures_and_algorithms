# title: longest-absolute-file-path
# detail: https://leetcode.com/submissions/detail/285266999/
# datetime: Wed Dec 11 23:07:17 2019
# runtime: 24 ms
# memory: 12.8 MB

class Solution:
    def lengthLongestPath(self, input: str) -> int:
        stack = []
        res = 0
        for file in input.split('\n'):
            indent = file.rfind('\t') + 1
            while len(stack) - 1 >= indent:
                stack.pop()
            l = len(file) - indent
            if stack:
                l += stack[-1]
            if '.' in file:
                if l > res:
                    res = l
            else:
                stack.append(l + 1)
        return res