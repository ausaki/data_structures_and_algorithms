# title: climbing-stairs
# detail: https://leetcode.com/submissions/detail/190659056/
# datetime: Tue Nov 20 14:07:52 2018
# runtime: 32 ms
# memory: N/A

class Solution:
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
#         if n == 0 or n == 1:
#             return 1
          
#         return self.climbStairs(n - 1) + self.climbStairs(n - 2)
        