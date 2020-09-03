# title: check-if-a-string-can-break-another-string
# detail: https://leetcode.com/submissions/detail/383118001/
# datetime: Wed Aug 19 15:49:24 2020
# runtime: 200 ms
# memory: 16.3 MB

class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        s2 = sorted(s2)
        flag = 0
        for i in range(len(s1)):
            f = ord(s1[i]) - ord(s2[i])
            if f == 0:
                continue
            if flag == 0:
                flag = f
            else:
                if f * flag < 0:
                    return False
        return True
            