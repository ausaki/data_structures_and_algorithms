# title: pow(x,-n)
# detail: https://leetcode.com/submissions/detail/275052709/
# datetime: Fri Nov  1 17:32:03 2019
# runtime: 36 ms
# memory: 13.7 MB

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        # if n % 2:
        #     return x * self.myPow(x * x, n // 2)
        # return self.myPow(x * x, n // 2)
        n, r = divmod(n, 2)
        p = self.myPow(x, n)
        if r:
            return p * p * x
        return p * p
        