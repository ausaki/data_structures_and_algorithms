# title: climbing-stairs
# detail: https://leetcode.com/submissions/detail/190660226/
# datetime: Tue Nov 20 14:13:44 2018
# runtime: 16 ms
# memory: N/A

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 1
        b = 1
        while n:
            a, b = b, a + b
            n -= 1
        return a