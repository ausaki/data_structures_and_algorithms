# title: remove-all-adjacent-duplicates-in-string
# detail: https://leetcode.com/submissions/detail/399731776/
# datetime: Thu Sep 24 00:36:28 2020
# runtime: 72 ms
# memory: 14 MB

class Solution:
    def removeDuplicates(self, S: str) -> str:
        s = []
        for c in S:
            if s and c == s[-1]:
                s.pop()
            else:
                s.append(c)
        return ''.join(s)