# title: isomorphic-strings
# detail: https://leetcode.com/submissions/detail/193991041/
# datetime: Sat Dec  8 18:21:28 2018
# runtime: 52 ms
# memory: 8.8 MB

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        charmap1 = [None] * 256
        charmap2 = [None] * 256
        length = len(s)
        for i in range(length):
            j = ord(s[i])
            if charmap1[j] is None:
                charmap1[j] = t[i]
                if charmap2[ord(t[i])] is None:
                    charmap2[ord(t[i])] = 1
                else:
                    return False
            else:
                c = charmap1[j]
                if c != t[i]:
                    return False
        return True
            
        