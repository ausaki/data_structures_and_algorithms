# title: add-digits
# detail: https://leetcode.com/submissions/detail/195726382/
# datetime: Tue Dec 18 15:57:28 2018
# runtime: 24 ms
# memory: 6.9 MB

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        d, r = divmod(num, 9)
        return r if r != 0 else 9
