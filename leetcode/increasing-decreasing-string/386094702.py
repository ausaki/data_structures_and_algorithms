# title: increasing-decreasing-string
# detail: https://leetcode.com/submissions/detail/386094702/
# datetime: Tue Aug 25 17:16:52 2020
# runtime: 64 ms
# memory: 13.9 MB

class Solution:
    def sortString(self, s: str) -> str:
        letters = [0] * 26
        a = ord('a')
        result = []
        for c in s:
            letters[ord(c) - a] += 1
        while len(result) < len(s):
            for i in range(26):
                if letters[i] > 0:
                    result.append(chr(i + a))
                    letters[i] -= 1
            for i in reversed(range(26)):
                if letters[i] > 0:
                    result.append(chr(i + a))
                    letters[i] -= 1
        return ''.join(result)