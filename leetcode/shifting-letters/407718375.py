# title: shifting-letters
# detail: https://leetcode.com/submissions/detail/407718375/
# datetime: Mon Oct 12 16:45:41 2020
# runtime: 168 ms
# memory: 17 MB

class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        result = list(S)
        s = 0
        for i in range(len(S) - 1, -1, -1):
            s = (s + shifts[i]) % 26
            result[i] = chr(97 + (ord(result[i]) - 97 + s) % 26)
        return ''.join(result)