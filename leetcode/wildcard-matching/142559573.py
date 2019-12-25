# title: wildcard-matching
# detail: https://leetcode.com/submissions/detail/142559573/
# datetime: Tue Feb 27 11:18:21 2018
# runtime: 100 ms
# memory: N/A

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_idx = 0
        p_idx = 0
        star_idx = -1
        ss_idx = -1
        
        s_len = len(s)
        p = p + '\x00'
        p_len = len(p)
        
        while s_idx < s_len:
            if p[p_idx] == '?' or s[s_idx] == p[p_idx]:
                s_idx += 1
                p_idx += 1
                continue
            if p[p_idx] == '*':
                star_idx = p_idx
                p_idx += 1
                ss_idx = s_idx
                continue
            # s 和 p 对应字符不匹配
            if star_idx >= 0:
                p_idx = star_idx + 1
                ss_idx += 1
                s_idx = ss_idx
                continue
            return False
        
        while p[p_idx] == '*' :
            p_idx += 1
            
        return not ord(p[p_idx])
            
            
        
        
        
        