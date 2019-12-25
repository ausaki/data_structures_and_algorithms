# title: add-digits
# detail: https://leetcode.com/submissions/detail/195724490/
# datetime: Tue Dec 18 15:45:08 2018
# runtime: 24 ms
# memory: 6.9 MB

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
            s = 0
            while num:
                num, r = divmod(num, 10)
                s += r
            num = s
        return num
