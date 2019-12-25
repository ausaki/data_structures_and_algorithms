# title: happy-number
# detail: https://leetcode.com/submissions/detail/193800394/
# datetime: Fri Dec  7 12:00:04 2018
# runtime: 36 ms
# memory: 6.9 MB

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = set()
        while n != 1:
            if n in s:
                return False
            s.add(n)
            sum = 0
            while n:
                n, r = divmod(n, 10)
                sum += r * r
            n = sum
        return True