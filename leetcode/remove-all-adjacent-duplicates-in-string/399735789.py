# title: remove-all-adjacent-duplicates-in-string
# detail: https://leetcode.com/submissions/detail/399735789/
# datetime: Thu Sep 24 00:48:08 2020
# runtime: 88 ms
# memory: 14.4 MB

class Solution:
    def removeDuplicates(self, S: str) -> str:
        s = list(S)
        i = -1
        for j in range(len(s)):
            if i >= 0 and s[j] == s[i]:
                i -= 1
            else:
                i += 1
                s[i] = s[j]
        return ''.join(s[:i + 1])