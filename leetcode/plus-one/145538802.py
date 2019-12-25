# title: plus-one
# detail: https://leetcode.com/submissions/detail/145538802/
# datetime: Sat Mar 17 16:39:17 2018
# runtime: 36 ms
# memory: N/A

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result = []
        carry = 1
        for d in digits[::-1]:
            s = d + carry
            carry, d = divmod(s, 10)
            result.insert(0, d)
        if carry != 0:
            result.insert(0, carry)
        return result
        