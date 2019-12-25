# title: add-digits
# detail: https://leetcode.com/submissions/detail/195727068/
# datetime: Tue Dec 18 16:01:54 2018
# runtime: 24 ms
# memory: 6.9 MB

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        return 0 if num == 0 else ((num-1) % 9) + 1
