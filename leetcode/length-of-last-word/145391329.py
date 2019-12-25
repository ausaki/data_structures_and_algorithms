# title: length-of-last-word
# detail: https://leetcode.com/submissions/detail/145391329/
# datetime: Fri Mar 16 14:54:18 2018
# runtime: 46 ms
# memory: N/A

class Solution(object):
    def lengthOfLastWord(self, string):
        """
        :type s: str
        :rtype: int
        """
        if not string:
            return 0
        s = -1
        e = -1
        l = 0
        for i, c in enumerate(string):
            if c == ' ':
                if s != -1 and e == -1:
                    e = i
                    l = e - s
                    s = -1
                    e = -1
            else:
                if s == -1:
                    s = i
        if s != -1 and e == -1:
            return i + 1 - s 
        return l
            
        
        