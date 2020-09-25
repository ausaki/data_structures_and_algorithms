# title: greatest-common-divisor-of-strings
# detail: https://leetcode.com/submissions/detail/399294062/
# datetime: Wed Sep 23 01:47:10 2020
# runtime: 40 ms
# memory: 13.8 MB

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) == len(str2) and str1 == str2:
            return str1
        if len(str2) < len(str1):
            str1, str2 = str2, str1
        while str2.startswith(str1):
            str2 = str2[len(str1):]
            if len(str2) < len(str1):
                str1, str2 = str2, str1
            if len(str1) == 0:
                return str2
        return ''
        