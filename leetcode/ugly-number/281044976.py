# title: ugly-number
# detail: https://leetcode.com/submissions/detail/281044976/
# datetime: Sat Nov 23 20:01:45 2019
# runtime: 32 ms
# memory: 12.6 MB

class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        while num > 1:
            n = num
            if num & 1 == 0:
                num = num >> 1
            if num % 3 == 0:
                num = num // 3
            if num % 5 == 0:
                num = num // 5
            if num == n:
                return False
        return True