# title: convert-a-number-to-hexadecimal
# detail: https://leetcode.com/submissions/detail/280065770/
# datetime: Tue Nov 19 15:53:55 2019
# runtime: 28 ms
# memory: 12.8 MB

class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        s = ''
        while num and len(s) < 8:
            num, r = divmod(num, 16)
            if r < 10:
                r = str(r)
            else:
                r = chr(ord('a') + r - 10)
            s = r + s
        return s
        