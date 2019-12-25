# title: ugly-number
# detail: https://leetcode.com/submissions/detail/195730401/
# datetime: Tue Dec 18 16:23:32 2018
# runtime: 24 ms
# memory: 6.9 MB

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        while num != 1:
            for i in [2, 3, 5]:
                if num % i == 0:
                    num = num / i
                    break
            else:
                return False
        return True