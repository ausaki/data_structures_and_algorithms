# title: gray-code
# detail: https://leetcode.com/submissions/detail/146349885/
# datetime: Thu Mar 22 12:00:46 2018
# runtime: 44 ms
# memory: N/A

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        return [i ^ (i >> 1) for i in xrange(1 << n)]
