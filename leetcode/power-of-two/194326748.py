# title: power-of-two
# detail: https://leetcode.com/submissions/detail/194326748/
# datetime: Mon Dec 10 14:07:07 2018
# runtime: 24 ms
# memory: 7 MB

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        for i in range(31):
            if 1 << i == n:
                return True
        return False