# title: sqrt(x)
# detail: https://leetcode.com/submissions/detail/145542727/
# datetime: Sat Mar 17 17:23:44 2018
# runtime: 197 ms
# memory: N/A

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        z = x / 2.0
        delta = z * z - x
        
        while abs(delta) >= 0.01:
            print z
            z -= delta / (2 * z)
            delta = z * z - x
            
        return int(z)
        