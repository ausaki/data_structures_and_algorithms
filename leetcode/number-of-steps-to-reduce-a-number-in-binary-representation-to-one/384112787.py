# title: number-of-steps-to-reduce-a-number-in-binary-representation-to-one
# detail: https://leetcode.com/submissions/detail/384112787/
# datetime: Fri Aug 21 16:16:17 2020
# runtime: 60 ms
# memory: 13.6 MB

class Solution:
    def numSteps(self, s: str) -> int:
        i = 0
        n = len(s)
        o = 0
        l = 0
        result = 0
        for i in range(n):
            if s[i] == '1':
                break
        for j in range(n - 1, -1, -1):
            if s[j] == '1':
                break
        result += n - j - 1
        for i in range(j, i - 1, -1):
            if s[i] == '0':
                o += 1
                if l != 0:
                    result += 1 + l
                    l = 1
            else:
                l += 1
                o = 0
        if l > 1:
            result += 1 + l 
        return result