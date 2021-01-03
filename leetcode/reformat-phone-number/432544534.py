# title: reformat-phone-number
# detail: https://leetcode.com/submissions/detail/432544534/
# datetime: Sun Dec 20 15:37:16 2020
# runtime: 32 ms
# memory: 14.3 MB

class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace(' ', '').replace('-', '')
        n = len(number)
        res = []
        for i in range(0, n, 3):
            if n - i == 4:
                res.append(number[i:i + 2])
                res.append(number[i + 2:])
                break
            else:
                res.append(number[i: i + 3])
        return '-'.join(res)