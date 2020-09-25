# title: remove-all-adjacent-duplicates-in-string-ii
# detail: https://leetcode.com/submissions/detail/395487516/
# datetime: Mon Sep 14 15:14:28 2020
# runtime: 124 ms
# memory: 15.4 MB

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if stack and c == stack[-1][0]:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([c, 1])
        return ''.join(c * n for c, n in stack)