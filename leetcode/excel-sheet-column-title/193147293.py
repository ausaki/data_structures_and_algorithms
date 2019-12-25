# title: excel-sheet-column-title
# detail: https://leetcode.com/submissions/detail/193147293/
# datetime: Mon Dec  3 23:25:57 2018
# runtime: 28 ms
# memory: N/A

import string
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = []
        charmap = string.ascii_uppercase
        while n :
            n, r =  divmod(n, 26)
            if r == 0:
                c = 'Z'
                n -= 1
            else:
                c = charmap[r - 1]
            result.append(c)
        return ''.join(reversed(result))
            