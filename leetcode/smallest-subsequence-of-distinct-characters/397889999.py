# title: smallest-subsequence-of-distinct-characters
# detail: https://leetcode.com/submissions/detail/397889999/
# datetime: Sat Sep 19 23:38:56 2020
# runtime: 44 ms
# memory: 13.8 MB

class Solution:
    def smallestSubsequence(self, text: str) -> str:
        last = {c: i for i, c in enumerate(text)}
        stack = []
        for i, c in enumerate(text):
            if c in stack:
                continue
            while stack and c < stack[-1] and last[stack[-1]] > i:
                stack.pop()
            stack.append(c)
        return ''.join(stack)