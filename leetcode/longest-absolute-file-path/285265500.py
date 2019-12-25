# title: longest-absolute-file-path
# detail: https://leetcode.com/submissions/detail/285265500/
# datetime: Wed Dec 11 22:55:14 2019
# runtime: 24 ms
# memory: 12.8 MB

class Solution:
    def lengthLongestPath(self, input: str) -> int:
        N = len(input)
        parts = []
        for item in input.split('\n'):
            l = len(item)
            item = item.lstrip('\t')
            parts.append((item, l - len(item)))
        stack = []
        i = 0
        res = 0
        for file, indent in parts:
            while stack and indent <= stack[-1][2]:
                stack.pop()
            l = len(file)
            if stack:
                l += stack[-1][1]
            if '.' in file:
                if l > res:
                    res = l
            else:
                stack.append([file, l + 1, indent])
        return res
        # while i < N:
        #     indent = 0
        #     while input[i] == '\t':
        #         indent += 1
        #         i += 1
        #     j = i
        #     while j < N and input[j] != '\n':
        #         j += 1
        #     file = input[i: j]
        #     while j < N and input[j] == '\n':
        #         j += 1
        #     i = j
        #     while stack and indent <= stack[-1][2]:
        #         stack.pop()
        #     l = len(file)
        #     if stack:
        #         l += stack[-1][1]
        #     if '.' in file:
        #         if l > res:
        #             res = l
        #     else:
        #         stack.append([file, l + 1, indent])
        return res