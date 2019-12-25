# title: pow(x,-n)
# detail: https://leetcode.com/submissions/detail/275052005/
# datetime: Fri Nov  1 17:25:54 2019
# runtime: 36 ms
# memory: 13.8 MB

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x * x, n // 2)
        return self.myPow(x * x, n // 2)
        