# title: pow(x,-n)
# detail: https://leetcode.com/submissions/detail/190613089/
# datetime: Tue Nov 20 10:17:57 2018
# runtime: 52 ms
# memory: N/A

class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        result = 1
        pos = 1
        if n < 0:
            pos = 0
            n = -(n + 1)
        n, r = divmod(n, 2)
        result = self.myPow(x, n)
        result *= result
        if r:
            result *= x
        if pos == 0:
            result *= x
            result = 1 / result
        return result;