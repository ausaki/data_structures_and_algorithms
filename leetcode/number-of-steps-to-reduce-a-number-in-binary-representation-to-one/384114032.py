# title: number-of-steps-to-reduce-a-number-in-binary-representation-to-one
# detail: https://leetcode.com/submissions/detail/384114032/
# datetime: Fri Aug 21 16:20:26 2020
# runtime: 36 ms
# memory: 13.8 MB

class Solution:
    def numSteps(self, s: str) -> int:
        i = 0
        n = len(s)
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
            if s[i] == '1':
                l += 1
            else:
                result += 1 + l
                l = 1
        if l > 1:
            result += 1 + l 
        return result