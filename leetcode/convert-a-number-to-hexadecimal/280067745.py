# title: convert-a-number-to-hexadecimal
# detail: https://leetcode.com/submissions/detail/280067745/
# datetime: Tue Nov 19 16:04:00 2019
# runtime: 28 ms
# memory: 12.7 MB

class Solution:
    def toHex(self, num: int) -> str:
        # if num == 0:
        #     return '0'
        # s = ''
        # while num and len(s) < 8:
        #     num, r = divmod(num, 16)
        #     if r < 10:
        #         r = str(r)
        #     else:
        #         r = chr(ord('a') + r - 10)
        #     s = r + s
        # return s
        if num == 0:
            return '0'
        mask = 0xf
        i = 0
        s = ''
        while num != 0 and i < 8:
            k = mask & num
            if k < 10:
                s = str(k) + s
            else:
                s = chr(ord('a') + k - 10) + s
            num >>= 4
            i += 1
        return s
        