# title: remove-k-digits
# detail: https://leetcode.com/submissions/detail/281528505/
# datetime: Mon Nov 25 15:30:04 2019
# runtime: 32 ms
# memory: 12.8 MB

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if num == '':
            return '0'
        N = len(num)
        i = 0
        while i < N - 1:
            if num[i] <= num[i + 1]:
                i += 1
                continue
            if k > 0:
                k -= 1
                num = num[:i] + num[i + 1:]
                N -= 1
                i -= 1
                if i < 0:
                    i = 0
            else:
                break
        if k > 0:
            num = num[:-k]
        num = num.lstrip('0')
        if num == '':
            return '0'
        return num 
                