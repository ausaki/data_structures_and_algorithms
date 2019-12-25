# title: excel-sheet-column-title
# detail: https://leetcode.com/submissions/detail/193146688/
# datetime: Mon Dec  3 23:20:43 2018
# runtime: 28 ms
# memory: N/A

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = []
        A = ord('A')
        while n :
            n, r =  divmod(n, 26)
            if r == 0:
                c = 'Z'
                n -= 1
            else:
                c = chr(A + r - 1)
            print(n, r, c)
            result.insert(0, c)
        return ''.join(result)
            