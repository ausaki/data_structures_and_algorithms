# title: check-if-a-string-can-break-another-string
# detail: https://leetcode.com/submissions/detail/383116300/
# datetime: Wed Aug 19 15:44:28 2020
# runtime: 144 ms
# memory: 16.1 MB

class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        s2 = sorted(s2)
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if s1[i] < s2[i]:
                    s1, s2 = s2, s1
                break
        for i in range(i, len(s1)):
            if s1[i] < s2[i]:
                return False
        return True
            