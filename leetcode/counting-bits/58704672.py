# title: counting-bits
# detail: https://leetcode.com/submissions/detail/58704672/
# datetime: Mon Apr 11 11:09:48 2016
# runtime: 696 ms
# memory: N/A

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = [0] * (num + 1)
        for i in range(0, num + 1):
            for k in range(0, 32):
                if (i & (0x1 << k)) > 0:
                    result[i] += 1
        return result