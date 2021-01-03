# title: maximum-binary-string-after-change
# detail: https://leetcode.com/submissions/detail/434761798/
# datetime: Sat Dec 26 23:03:55 2020
# runtime: 76 ms
# memory: 15.7 MB

class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        i = binary.find('0')
        if i == -1:
            return binary
        a, b = binary.count('0', i), binary.count('1', i)
        binary = binary[:i]
        if a > 1:
            binary += '1' * (a - 1) + '0'
        elif a > 0:
            binary += '0'
        binary += '1' * b
        return binary
        
        
        