# title: reformat-phone-number
# detail: https://leetcode.com/submissions/detail/432446995/
# datetime: Sun Dec 20 10:41:29 2020
# runtime: 36 ms
# memory: 14.2 MB

class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace(' ', '').replace('-', '')
        n = len(number)
        res = []
        for i in range(0, n, 3):
            if n - i == 1:
                if res:
                    l = res.pop() + number[i]
                    res.append(l[:2])
                    res.append(l[2:])
                else:
                    res.append(number[i])
            else:
                res.append(number[i: i + 3])
        return '-'.join(res)