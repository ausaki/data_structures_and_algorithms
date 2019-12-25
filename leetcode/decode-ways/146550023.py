# title: decode-ways
# detail: https://leetcode.com/submissions/detail/146550023/
# datetime: Fri Mar 23 16:23:16 2018
# runtime: 56 ms
# memory: N/A

class Solution(object):
    def __init__(self):
        self._cache = {
            0: 0,
        }
        
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        c = 0
        
        if l in self._cache:
            return self._cache[l]
        
        if l == 1:
            if 1 <= int(s[0]) <= 26:
                c = 1
            else:
                c = 0
            self._cache[l] = c
            return c
            
        
        # if l == 2:
        #     if 1 <= int(s[:2]) <= 26:
        #         return 2
        #     return 1
        
        a = int(s[0])
        b = int(s[1])
        if 1 <= a <= 26:
            c += self.numDecodings(s[1:])
        
        if a != 0 and 1 <= a * 10 + b <= 26:
            if l == 2:
                c += 1
            else:
                c += self.numDecodings(s[2:])
        self._cache[l] = c
        return c
        