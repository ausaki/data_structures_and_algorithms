# title: check-if-number-is-a-sum-of-powers-of-three
# detail: https://leetcode.com/submissions/detail/464298901/
# datetime: Sun Mar  7 00:41:47 2021
# runtime: 36 ms
# memory: 14.2 MB

class Solution:
        
    def checkPowersOfThree(self, n: int) -> bool:
        r = 0
        while r == 0:
            n, r = divmod(n, 3)
        if r != 1:
            return False
        if n == 0:
            return True
        return self.checkPowersOfThree(n)
            